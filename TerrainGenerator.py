
def biomize(elevation, temperature, side):
    final = [[[0, 0, 0] for i in range(j)] for j in elevation]
    half = side // 2
    i = half
    j = half
    while i < len(elevation):
        while j < len(elevation[0]):
            ele = elevation[i, j][0]
            temp = temperature[i, j][0]
            final[i - half:i + half, j - half:j + half] = terrain_picker(val)
            j += side
        i += side
        j = half

    i = 0
    while i < len(arr):
        arr[:, i] = [0, 0, 0]
        arr[i, :] = [0, 0, 0]
        i += side
    return arr

