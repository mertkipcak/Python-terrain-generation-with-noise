import cv2 as cv
import numpy as np

def interpolant(t):
    return t * t * t * (t * (t * 6 - 15) + 10)


def generate_perlin_noise_2d(
        shape, res, tileable=(False, False), interpolant=interpolant
):
    """Generate a 2D numpy array of perlin noise.
    Args:
        shape: The shape of the generated array (tuple of two ints).
            This must be a multple of res.
        res: The number of periods of noise to generate along each
            axis (tuple of two ints). Note shape must be a multiple of
            res.
        tileable: If the noise should be tileable along each axis
            (tuple of two bools). Defaults to (False, False).
        interpolant: The interpolation function, defaults to
            t*t*t*(t*(t*6 - 15) + 10).
    Returns:
        A numpy array of shape shape with the generated noise.
    Raises:
        ValueError: If shape is not a multiple of res.
    """
    delta = (res[0] / shape[0], res[1] / shape[1])
    d = (shape[0] // res[0], shape[1] // res[1])
    grid = np.mgrid[0:res[0]:delta[0], 0:res[1]:delta[1]] \
               .transpose(1, 2, 0) % 1
    # Gradients
    angles = 2 * np.pi * np.random.rand(res[0] + 1, res[1] + 1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))
    if tileable[0]:
        gradients[-1, :] = gradients[0, :]
    if tileable[1]:
        gradients[:, -1] = gradients[:, 0]
    gradients = gradients.repeat(d[0], 0).repeat(d[1], 1)
    g00 = gradients[:-d[0], :-d[1]]
    g10 = gradients[d[0]:, :-d[1]]
    g01 = gradients[:-d[0], d[1]:]
    g11 = gradients[d[0]:, d[1]:]
    # Ramps
    n00 = np.sum(np.dstack((grid[:, :, 0], grid[:, :, 1])) * g00, 2)
    n10 = np.sum(np.dstack((grid[:, :, 0] - 1, grid[:, :, 1])) * g10, 2)
    n01 = np.sum(np.dstack((grid[:, :, 0], grid[:, :, 1] - 1)) * g01, 2)
    n11 = np.sum(np.dstack((grid[:, :, 0] - 1, grid[:, :, 1] - 1)) * g11, 2)
    # Interpolation
    t = interpolant(grid)
    n0 = n00 * (1 - t[:, :, 0]) + t[:, :, 0] * n10
    n1 = n01 * (1 - t[:, :, 0]) + t[:, :, 0] * n11
    return np.sqrt(2) * ((1 - t[:, :, 1]) * n0 + t[:, :, 1] * n1)


def fn(x):
    return int((x + 1) * 122)


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
            arr[i-half:i+half, j-half:j+half] = terrain_picker(val)
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
    fin = np.zeros((1000, 1000, 3), dtype='uint8')
    arr = [[fn(j) for j in i] for i in generate_perlin_noise_2d((1000, 1000), (5, 5))]
    for i in range(1000):
        for j in range(1000):
            fin[i][j][0] += arr[i][j]

    cv.imshow('noise', fin)
    cv.imshow('img', transform_block(fin, 10))
    cv.waitKey(0)
