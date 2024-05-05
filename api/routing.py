from PIL import Image
from ultralytics import YOLO
import segmentation_models_pytorch as smp
from ml.models.segmentation.utils import CLASSES_IDS_TO_COLORS_DICT, CLASSES_INFO_DICT
from datetime import datetime
import os.path
import numpy as np
import torch
import torch.nn as nn
from api import app
from flask import jsonify, request
from api import db
from sqlalchemy import select, insert
from api.models import User, AnalysisResult
from werkzeug.security import generate_password_hash, check_password_hash


@app.post('/model_api/get_prediction')
def model():
    timestamp_dttm = datetime.now()
    timestamp = timestamp_dttm.strftime('%Y%m%d_%H%M%S')

    data = request.get_json()

    ml_task_flags = data['ml_task_flags']

    width, height = data['width'], data['height']
    img_data = np.array(list(data['image'].values())).astype('uint8')
    R, G, B = (
        img_data[0::4].reshape(height, width)
        , img_data[1::4].reshape(height, width)
        , img_data[2::4].reshape(height, width)
    )

    image = np.transpose(np.stack([R, G, B], axis=0), (1, 2, 0))
    pil_image = Image.fromarray(image)

    gallery_dir = '../app/images_gallery'
    if not os.path.exists(gallery_dir):
        os.mkdir(gallery_dir)

    path_detection = None

    if ml_task_flags['buildings_detection']:
        yolo = YOLO('model_weights/yolo8_weights.pt')
        pil_image.resize((640, 640)).save('detection_tmp.png')
        result = yolo(['detection_tmp.png'])
        img_detection = result[0].plot(font_size=12, pil=True, labels=True, line_width=2)
        path_detection = f'{gallery_dir}/detection{timestamp}.png'
        Image.fromarray(img_detection).resize((1024, 1024)).save(path_detection)

    unet = smp.Unet(
        encoder_name='resnet50',
        encoder_weights='imagenet',
        in_channels=3,
        classes=6
    )

    unet.load_state_dict(torch.load('model_weights/unet_resnet50_imagenet_320.pth'))

    image_segmentation = np.array(pil_image.resize((320, 320)))
    outputs = unet(torch.tensor(np.transpose(image_segmentation, (2, 0, 1))).float().unsqueeze(0))
    softmax = nn.Softmax(dim=1)
    preds = torch.argmax(softmax(outputs), dim=1)[0].numpy()

    new_preds = np.ndarray(shape=(preds.shape[0], preds.shape[1], 3), dtype='uint8')

    ignore_keys = {'buildings_detection'}
    to_make_null = {
        CLASSES_INFO_DICT[item]['code'] for item in ml_task_flags
        if not ml_task_flags[item] and item not in ignore_keys
    }

    for j in range(0, preds.shape[0]):
        for k in range(0, preds.shape[1]):
            new_preds[j][k] = CLASSES_IDS_TO_COLORS_DICT[preds[j][k]] if preds[j][k] not in to_make_null \
                else CLASSES_IDS_TO_COLORS_DICT[0]

    init_image = Image.fromarray(image_segmentation).convert("RGBA")
    segm_result = Image.fromarray(new_preds).convert("RGBA")
    segm_result.putalpha(160)

    init_image.paste(segm_result, (0, 0), segm_result)
    init_image = init_image.resize((1024, 1024))

    path_segmentation = f'{gallery_dir}/segmentation{timestamp}.png'
    init_image.save(path_segmentation)

    path_mask = f'{gallery_dir}/mask{timestamp}.png'
    segm_result.resize((1024, 1024)).save(path_mask)

    path_original = f'{gallery_dir}/original{timestamp}.png'
    pil_image.resize((1024, 1024)).save(path_original)

    skip_path_elems = 7

    user_id = data['user_id']

    prefix = '../' * 2

    db.session.execute(
        insert(AnalysisResult)
        , [
            {
                'user_id': user_id
                , 'created_dttm': timestamp_dttm
                , 'segmentation_image': prefix + path_segmentation[skip_path_elems:]
                , 'detection_image': prefix + path_detection[skip_path_elems:] if path_detection else None
                , 'original_image': prefix + path_original[skip_path_elems:]
            }
        ]
    )
    db.session.commit()

    return jsonify({
        'path_segmentation': prefix + path_segmentation[skip_path_elems:]
        , 'path_detection': prefix + path_detection[skip_path_elems:] if path_detection else None
        , 'path_mask_only': prefix + path_mask[skip_path_elems:]
    }), 201


@app.post('/user_api/register')
def register_user():
    data = request.get_json()
    login = data['login']
    user_data = db.session.execute(select(User).where(User.login == login)).first()

    if user_data:
        return data, 409

    password = data['password']
    user = db.session.execute(
        insert(User).returning(User)
        , [
            {
                'login': login
                , 'password_hash': generate_password_hash(password)
            }
        ]
    ).first()[0]

    db.session.commit()

    return jsonify({"user_id": user.user_id, "login": login}), 201


@app.post('/user_api/login')
def login_user():
    data = request.get_json()
    login = data['login']
    user_data = db.session.execute(select(User).where(User.login == login)).first()

    if not user_data:
        return jsonify({'auth_error': 'Пользователя с указанным логином не существует'}), 401
    else:
        user = user_data[0]
        password = data['password']

        if check_password_hash(user.password_hash, password):
            return jsonify({"user_id": user.user_id, "login": login}), 200
        else:
            return jsonify({'auth_error': 'Неверный пароль пользователя'}), 401


@app.get('/analysis_api/analysis_history')
def get_user_history():
    user_id = request.args.get('user_id')
    analysis_data = db.session.scalars(
        select(AnalysisResult)
        .where(AnalysisResult.user_id == user_id)
        .order_by(AnalysisResult.created_dttm.desc())
    )

    data = []
    for idx, item in enumerate(analysis_data, start=1):
        data.append({
            'new_id': idx
            , 'created_dttm': item.created_dttm
            , 'segmentation_image': item.segmentation_image
            , 'detection_image': item.detection_image
            , 'original_image': item.original_image
        })

    return jsonify(data), 200


@app.get('/analysis_api/analysis_info')
def get_analysis():
    user_id = request.args.get('user_id')
    analysis_id = request.args.get('analysis_id')

    analysis_result = db.session.scalars(
        select(AnalysisResult)
        .where((AnalysisResult.user_id == user_id) & (AnalysisResult.analysis_id == analysis_id))
        .order_by(AnalysisResult.created_dttm.desc())
    ).first()

    return jsonify({
        'created_dttm': analysis_result.created_dttm
        , 'segmentation_image': analysis_result.segmentation_image
        , 'detection_image': analysis_result.detection_image
        , 'original_image': analysis_result.original_image
    }), 200