moves = open("testinput2.txt", "r").read().split("\n")
head, tail = [0, 0], [0, 0]
directions = {"R": [0, 1], "L": [0, -1], "U": [1, 1], "D": [1, -1]}
tailPlaces = []

for move in moves:
    [direction, count] = move.split(' ')
    for nr in range(int(count)):
        head[directions[direction][0]] += directions[direction][1]
        tailPlaces.append(tail[:])

        diff_col = head[0] - tail[0]
        diff_row = head[1] - tail[1]
        if not (diff_col in [-1, 0, 1] and diff_row in [-1, 0, 1]):
            if diff_col == 0 or diff_row == 0:
                tail[directions[direction][0]] += directions[direction][1]
            else:
                diff_col = -1 if diff_col < 0 else 1
                diff_row = -1 if diff_row < 0 else 1
                tail[0] += diff_col
                tail[1] += diff_row

drawing = []
for row in range(-20, 20):
    line = ""
    for col in range(-20, 20):
        if col == 0 and row == 0:
            line += 's'
        elif [col, row] in tailPlaces:
            line += '#'
        else:
            line += '.'
    drawing.append(line)
print("\n".join(reversed(drawing)))

print("first puzzle answer = " + str(len(set(map(lambda pos: str(pos), tailPlaces)))))
print("second puzzle answer = " + str(0))