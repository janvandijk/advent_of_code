commands = open("input.txt", "r").read().splitlines()

rope_length = 10
rope = [(0,0) for i in range(rope_length)]
all_seen = [{(0,0)} for i in range(rope_length)]

moves = {"R":(1,0), "U":(0,1), "L":(-1, 0), "D":(0,-1)}
def move(point, dir):
    return (point[0] + moves[dir][0], point[1] + moves[dir][1])

for command in commands:
    dir, length = command.split(" ")
    for i in range(0, int(length)):
        rope[0] = move(rope[0], dir)
        for i in range(1, rope_length):
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
            all_seen[i].add(rope[i])
                    
print(len(all_seen[1]))
print(len(all_seen[-1]))
