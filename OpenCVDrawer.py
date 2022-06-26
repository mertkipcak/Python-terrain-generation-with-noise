import numpy as np
import cv2 as cv


def draw_grid(grid, side=10, grid_color=(0, 0, 0)):
    # Set up the grid to draw on with 5*5 pixels for each element of the input grid
    wg = len(grid)
    wh = len(grid[0])
    w = len(grid) * (side+1) + 1
    h = len(grid[0]) * (side+1) + 1
    fin = np.zeros((w, h, 3), dtype='uint8')
    fin[-1, :] = grid_color
    for i in range(wg):
        fin[i * (side+1), :] = grid_color
    fin[:, -1] = grid_color
    for i in range(wh):
        fin[:, i * (side+1)] = grid_color

    for i in range(wg):
        for j in range(wh):
            for w in range(side):
                for h in range(side):
                    fin[(side+1)*i+w+1][(side+1)*j+h+1] = grid[i][j]

    cv.imshow('grid', fin)
    cv.waitKey(0)
