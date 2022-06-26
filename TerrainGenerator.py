import numpy as np


def terrain_picker(val):
    if val < 40:
        return [200, 0, 0]
    elif val < 100:
        return [250, 50, 0]
    elif val < 120:
        return [250, 140, 0]
    elif val < 135:
        return [64, 212, 245]
    elif val < 165:
        return [10, 200, 10]
    elif val < 195:
        return [0, 100, 0]
    elif val < 210:
        return [64, 70, 84]
    else:
        return [255, 255, 255]


def temp_biome(temp, picker=terrain_picker):
    w = len(temp)
    h = len(temp[0])
    ret = np.zeros((w, w, 3), dtype='uint8')
    for i in range(w):
        for j in range(h):
            ret[i][j] = picker(temp[i][j])
    return ret
