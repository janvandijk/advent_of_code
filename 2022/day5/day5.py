import re
import queue

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

# inlezen stacks
temp_stacks = []
line_index = 0
while(True):
    line = lines[line_index]
    line_index += 1
    if line == "":
        break
    print(line)
    stack_index = 0
    for x in line:
        if len(temp_stacks) < stack_index + 1:
            temp_stacks.append(queue.LifoQueue())
        temp_stacks[stack_index].put(x)

        stack_index += 1

# opschonen stacks
stacks = []
stack_index = 0
while(stack_index < len(temp_stacks)):
    if ((stack_index) % 4 == 1):
        new_queue = queue.LifoQueue()
        while(not temp_stacks[stack_index].empty()):
            x = temp_stacks[stack_index].get()
            if not x == " ":
                new_queue.put(x) 
        stacks.append(new_queue)

    stack_index += 1

while (line_index < len(lines)):
    print(lines[line_index])
    [(m, f, t)] = re.findall("move (\d+) from (\d+) to (\d+)", lines[line_index])

    move = int(m)
    frm = int(f) - 1
    to = int(t) - 1

    print('m {} f {} to {} '.format(move, frm, to), end='')

    while(move > 0):
        print(".", end='')
        x = stacks[frm].get()
        stacks[to].put(x)
        move -= 1
    
    print("")

    line_index += 1

for stack in stacks:
    print(stack.get(), end='')

