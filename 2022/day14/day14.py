import numpy as np

scan_lines = [line for line in open("testinput.txt", "r").read().splitlines() if line != ""]

print(scan_lines)

draw = [".", "#", "o", "+"]

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

print(lines)
print(min_x, min_y, max_x, max_y)

max_y += 2

min_x -= (max_x - min_x) + 1
max_x += (max_x - min_x) + 1


cave = np.zeros((max_x + 1 - min_x,max_y + 1), dtype = int)

for x in range(max_x + 1 - min_x):
    cave[x][max_y] = "1"


print(cave)
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

for y in range(min_y, max_y + 1):
    for x in range(0, max_x - min_x + 1):
        print(draw[cave[x][y]], end="")
    print()

for x in range(100_000):

    print(f"Sand: {x}")
    # for y in range(min_y, max_y + 1):
    #     for x in range(0, max_x - min_x + 1):
    #         print(draw[cave[x][y]], end="")
    #     print()

    sand = (500,0)
    x,y = sand
    x = x - min_x

    if cave[x][y] > 0:
        break

    while(True):
        if cave[x][y + 1] == 0:
            y += 1
            continue
#        if cave[x - 1][y] == 0:
        if cave[x - 1][y + 1] == 0:
            # if cave[x - 1][y + 2] == 0:
            #     x -= 1
            #     continue
            # cave[x - 1][y + 1] = 2
            # break
            x -= 1
            continue
        if cave[x + 1][y + 1] == 0:
            # if cave[x + 1][y + 2] == 0:
            #     x += 1
            #     continue
            # cave[x + 1][y + 1] = 2
            # break
            x += 1
            continue
        cave[x][y] = 2
        break

for y in range(min_y, max_y + 1):
    for x in range(0, max_x - min_x + 1):
        print(draw[cave[x][y]], end="")
    print()
