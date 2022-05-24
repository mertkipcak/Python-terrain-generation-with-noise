import cv2 as cv
import numpy as np
import NoiseGenerator

def transform(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j][0] < 100:
                arr[i][j] = [230, 100, 0]
            elif arr[i][j][0] < 180:
                arr[i][j] = [0, 250, 0]
            else:
                arr[i][j] = [255, 255, 255]
    return arr


def transform_block(arr, side):
    half = side // 2
    i = half
    j = half

    while i < len(arr):
        while j < len(arr[0]):
            val = arr[i, j][0]
            arr[i - half:i + half, j - half:j + half] = terrain_picker(val)
            j += side
        i += side
        j = half

    i = 0
    while i < len(arr):
        arr[:, i] = [0, 0, 0]
        arr[i, :] = [0, 0, 0]
        i += side
    return arr


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


def transform_topography(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j][0] % 10 == 0:
                arr[i][j] = [0, 0, 0]
            else:
                arr[i][j] = [255, 255, 255]
    return arr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    size = 3000
    fin = np.zeros((size, size, 3), dtype='uint8')
    for i in range(size):
        for j in range(size):
            fin[i][j][0] += arr[i][j]

    cv.imshow('noise', fin)
    cv.imshow('img', transform_block(fin, 20))
    cv.waitKey(0)
