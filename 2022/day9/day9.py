commands = open("input.txt", "r").read().splitlines()

head = (0,0)
tail = (0,0)

all_seen = {tail}

for command in commands:
    dir,length = command.split(" ")
    print("{} - {} ".format(dir,length))
    for i in range(0, int(length)):
        print("Head: {} Tail: {}".format(head, tail))
        old_head = head
        if dir == "R":
            head = (head[0] + 1, head[1])
        if dir == "L":
            head = (head[0] - 1, head[1])
        if dir == "U":
            head = (head[0], head[1] + 1)
        if dir == "D":
            head = (head[0], head[1] -1)
        print("Diffs: {} - {}".format(head[0] - tail[0], head[1] - tail[1]))
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            tail = old_head
            all_seen.add(tail)
            print("Len: {}".format(len(all_seen)))

print(len(all_seen))

