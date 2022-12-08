import numpy as np

forest_input = open("input.txt", "r").read().splitlines()
w, h =  len(forest_input[0]), len(forest_input)
forest = np.empty((w,h), dtype = int)
for x in range(0, w):
    for y in range(0, h):
        forest[x][y] = forest_input[x][y]

highest_trees = np.zeros((w,h), dtype = int)
for x in range(0, w):
    start, finish = -1, -1
    for y in range(0, h):
        if start < forest[x][y]:
            highest_trees[x][y] = 1
            start = forest[x][y]
        if finish < forest[x][h - y - 1]:
            highest_trees[x][h - y - 1] = 1
            finish = forest[x][h - y - 1]

for y in range(0, h):
    start, finish = -1, -1
    for x in range(0, w):
        if start < forest[x][y]:
            highest_trees[x][y] = 1
            start = forest[x][y]
        if finish < forest[w - x - 1][y]:
            highest_trees[w - x - 1][y] = 1
            finish = forest[w - x - 1][y]

print("Aantal hoogste bomen: {}".format(sum(highest_trees.flatten())))

score = 0
for x in range(0, w):
    for y in range(0, h):
        height = forest[x][y]
        left,right,top,bottom = 0,0,0,0

        # search left
        for i in range(x-1,-1,-1):
            left += 1
            if forest[i][y] >= height:
                break

        # search right
        for i in range(x+1,w):
            right += 1
            if forest[i][y] >= height:
                break

        # search top
        for i in range(y-1,-1,-1):
            top += 1
            if forest[x][i] >= height:
                break

        # search bottom
        for i in range(y+1,h):
            bottom += 1
            if forest[x][i] >= height:
                break            

        if left * right * top * bottom > score:
            score = left * right * top * bottom

print("Best viewscore: {}".format(score))
