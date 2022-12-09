commands = open("input.txt", "r").read().splitlines()

rope = []
rope_length = 10

all_seen = {(0,0)}

for i in range(0,rope_length):
    rope.append((0,0))

def visualize():
    for y in range(-20,20):
        for x in range(-20,20):
            char = "."
            for i in range(rope_length-1, -1, -1):
                if rope[i] == (x,y):
                    char = i
            print(char, end="")
        print()
    print()

def move(point,dir):
    if dir == "R":
        return (point[0] + 1, point[1])
    if dir == "L":
        return (point[0] -1, point[1])
    if dir == "U":
        return (point[0], point[1] + 1)
    if dir == "D":
        return (point[0], point[1] - 1)


for command in commands:
    print("Command: " + command)
    dir,length = command.split(" ")
    for i in range(0, int(length)):
        rope[0] = move(rope[0], dir)
        # move rest of the rope
        for i in range(1, rope_length):
            # move diagonally?
            if abs(rope[i-1][0] - rope[i][0]) + abs(rope[i-1][1] - rope[i][1]) > 2:
                if rope[i-1][0] - rope[i][0] < 0:
                    rope[i] = move(rope[i],"L")
                else: 
                    rope[i] = move(rope[i],"R")
                if rope[i-1][1] - rope[i][1] < 0:
                    rope[i] = move(rope[i],"D")
                else: 
                    rope[i] = move(rope[i],"U")
            else:        
                if rope[i-1][0] - rope[i][0] > 1:
                    rope[i] = move(rope[i],"R")
                if rope[i-1][0] - rope[i][0] < -1:
                    rope[i] = move(rope[i],"L")
                if rope[i-1][1] - rope[i][1] > 1:
                    rope[i] = move(rope[i],"U")
                if rope[i-1][1] - rope[i][1] < -1:
                    rope[i] = move(rope[i],"D")
            if i == rope_length -1:
                all_seen.add(rope[i])
                    

    #     visualize()
    # input("enter")


print(len(all_seen))

