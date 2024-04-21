import os.path

import numpy as np
import torch
import torch.nn as nn
from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image
from ultralytics import YOLO
import segmentation_models_pytorch as smp
from ml.models.segmentation.utils import CLASSES_IDS_TO_COLORS_DICT
from datetime import datetime

app = Flask(__name__)

CORS(app)


@app.post('/model_api/get_prediction')
def model():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    data = request.get_json()
    width, height = data['width'], data['height']
    img_data = np.array(list(data['image'].values())).astype('uint8')
    R, G, B = (
        img_data[0::4].reshape(height, width)
       , img_data[1::4].reshape(height, width)
       , img_data[2::4].reshape(height, width)
    )

    image = np.transpose(np.stack([R, G, B], axis=0), (1, 2, 0))
    pil_image = Image.fromarray(image)

    yolo = YOLO('model_weights/yolo8_weights.pt')
    pil_image.resize((640, 640)).save('detection_tmp.png')
    result = yolo(['detection_tmp.png'])
    img_detection = result[0].plot(font_size=12, pil=True, labels=True, line_width=2)

    gallery_dir = '../app/images_gallery'
    if not os.path.exists(gallery_dir):
        os.mkdir(gallery_dir)

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

    for j in range(0, preds.shape[0]):
        for k in range(0, preds.shape[1]):
            new_preds[j][k] = CLASSES_IDS_TO_COLORS_DICT[preds[j][k]]

    init_image = Image.fromarray(image_segmentation).convert("RGBA")
    segm_result = Image.fromarray(new_preds).convert("RGBA")
    segm_result.putalpha(160)

    init_image.paste(segm_result, (0, 0), segm_result)
    init_image = init_image.resize((1024, 1024))

    path_segmentation = f'{gallery_dir}/segmentation{timestamp}.png'
    init_image.save(path_segmentation)

    path_mask = f'{gallery_dir}/mask{timestamp}.png'
    segm_result.resize((1024, 1024)).save(path_mask)

    skip_path_elems = 7
    return jsonify({
        'path_segmentation': path_segmentation[skip_path_elems:]
        , 'path_detection':  path_detection[skip_path_elems:]
        , 'path_mask_only': path_mask[skip_path_elems:]
    })


if __name__ == '__main__':
    app.run()