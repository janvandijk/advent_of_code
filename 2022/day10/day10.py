import numpy as np
instructions = open("input.txt", "r").read().splitlines()

x = 1
cycle = 0
som = 0
threshold = 20

screen =  np.zeros((40,6), dtype=int)
index = 0

def cycle_and_check():
    global cycle
    global threshold
    global som
    global x
    global index
    global screen

    print("index: {} ({},{}) x: {} - Draw: {}".format(index, index % 40, int(index/40), x, abs(index % 40 - x ) < 2 ))

    if abs(index % 40 - x ) < 2:
        screen[index % 40][int(index / 40)] = 1
    index +=1

    cycle += 1
    if cycle == threshold:
        som += cycle * x
        print("Cycle: {} - x: {} - Signal: {} - Sum: {}".format(cycle,x,cycle * x,som))
        threshold += 40
        print(screen)
        input("verder")


for command in instructions:
    if command == "noop":
        cycle_and_check()
        continue
    cycle_and_check()
    _, value = command.split(" ")
    cycle_and_check()
    x += int(value)
    continue
    
print(screen)

for y in range(6):
    for x in range(40):
        if screen[x][y] == 1:
            print("#", end="")
        else: 
            print(" ", end="")
    print()
        