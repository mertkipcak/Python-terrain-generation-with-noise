from NoiseGenerator import generate_noise
from OpenCVDrawer import draw_grid
from TerrainGenerator import temp_biome


if __name__ == '__main__':
    grid = generate_noise((100, 100), (5, 5))
    grid = temp_biome(grid)
    draw_grid(grid)

