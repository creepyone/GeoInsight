import numpy as np

CLASSES_INFO_DICT = {
    'None': {
        'alter_name': 'Пусто'
        , 'code': 0
    }
    , 'Agriculture': {
        'alter_name': 'Агрозона'
        , 'code': 1
    }
    , 'Trees': {
        'alter_name': 'Лес'
        , 'code': 2
    }
    , 'Building': {
        'alter_name': 'Здание'
        , 'code': 3
    }
    , 'Road': {
        'alter_name': 'Дорога'
        , 'code': 4
    }
    , 'Water': {
        'alter_name': 'Вода'
        , 'code': 5
    }
}


CLASSES_IDS_TO_LABELS_DICT = {
    0: 'Пусто'
    , 1: 'Агрозона'
    , 2: 'Лес'
    , 3: 'Здание'
    , 4: 'Дорога'
    , 5: 'Вода'
}


CLASSES_IDS_TO_COLORS_DICT = {
    0: [255, 255, 255]
    , 1: [255, 255, 0]
    , 2: [74, 103 ,65]
    , 3: [155, 118, 83]
    , 4: [105, 105, 105]
    , 5: [0, 0, 255]
}

class InputStream:
    def __init__(self, data):
        self.data = data
        self.i = 0

    def read(self, size):
        out = self.data[self.i: self.i + size]
        self.i += size
        return int(out, 2)


def access_bit(data, num):
    base = int(num // 8)
    shift = 7 - int(num % 8)
    return (data[base] & (1 << shift)) >> shift


def bytes2bit(data):
    return ''.join([str(access_bit(data, i)) for i in range(len(data) * 8)])


def decode_rle(rle, print_params: bool = False):
    input = InputStream(bytes2bit(rle))
    num = input.read(32)
    word_size = input.read(5) + 1
    rle_sizes = [input.read(4) + 1 for _ in range(4)]

    if print_params:
        print(
            'RLE params:', num, 'values', word_size, 'word_size', rle_sizes, 'rle_sizes'
        )

    i = 0
    out = np.zeros(num, dtype=np.uint8)
    while i < num:
        x = input.read(1)
        j = i + 1 + input.read(rle_sizes[input.read(2)])
        if x:
            val = input.read(word_size)
            out[i:j] = val
            i = j
        else:
            while i < j:
                val = input.read(word_size)
                out[i] = val
                i += 1
    return out
