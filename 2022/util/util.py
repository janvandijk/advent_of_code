import numpy as np


def printGrid(grid, drawChars = None):
    width = len(grid)
    height = len(grid[0])
    for y in range(0, height):
        for x in range(0, width):
            if drawChars:
                print(drawChars[grid[x][y]], end="")
            else:
                print(grid[x][y], end="")
        print()