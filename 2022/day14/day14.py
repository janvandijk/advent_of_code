import sys
import numpy as np
sys.path.append('../util')
import util

draw = [".", "#", "o"]

# parse input to lines
scan_lines = [line for line in open("input.txt", "r").read().splitlines() if line != ""]
lines = []
min_x, min_y, max_x, max_y = 500,0,500,0
for scan_line in scan_lines:
    points = scan_line.split(" -> ")
    from_point = None
    for point in points:
        x,y = (int(x) for x in point.split(","))
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        to_point = (x,y)
        if from_point != None:
            lines.append([from_point, to_point])
        from_point = to_point


# extend grid 2 in y direction and double in x direction
max_y += 2
min_x -= (max_x - min_x) + 1
max_x += (max_x - min_x) + 1

# add bottom line
cave = np.zeros((max_x + 1 - min_x,max_y + 1), dtype = int)
for x in range(max_x + 1 - min_x):
    cave[x][max_y] = "1"

# draw other lines
for line in lines:
    (from_point_x, from_point_y), (to_point_x, to_point_y) = line
    if from_point_x < to_point_x:
        for x in range(from_point_x, to_point_x + 1):
            cave[x- min_x][from_point_y] = 1
    if to_point_x < from_point_x:
        for x in range(to_point_x, from_point_x + 1):
            cave[x- min_x][from_point_y] = 1
    if from_point_y < to_point_y:
        for y in range(from_point_y, to_point_y + 1):
            cave[from_point_x- min_x][y] = 1
    if to_point_y < from_point_y:
        for y in range(to_point_y, from_point_y + 1):
            cave[from_point_x- min_x][y] = 1

# let the sand fall
for sand_count in range(100_000):
    x, y = 500-min_x, 0

    if cave[x][y] > 0:
        break

    while(True):
        if cave[x][y + 1] == 0:
            y += 1
            continue
        if cave[x - 1][y + 1] == 0:
            x -= 1
            continue
        if cave[x + 1][y + 1] == 0:
            x += 1
            continue
        cave[x][y] = 2
        break

print(f"Sand: {sand_count}")
util.printGrid(cave, draw)
