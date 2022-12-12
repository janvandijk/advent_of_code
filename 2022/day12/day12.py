import collections

start, end = "S", "E"
def valueOf(char):
    if char == start:
        return 0
    if char == end:
        return 25
    return ord(char) - ord('a')    

directions = [(0,-1),(0,1),(-1,0),(1,0)]
def find_shortest(start, grid, end):
    width, height =  len(grid[0]), len(grid)
    seen = set(start)
    queue = collections.deque()
    queue.append(([start], start))
    while queue:
        path, (x, y) = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height or (new_x, new_y) in seen:
                continue
            if (valueOf(grid[new_y][new_x]) - valueOf(grid[y][x])) < 2:
                queue.append((path + [(new_x, new_y)], (new_x, new_y)))
                seen.add((new_x,new_y))

grid = open("input.txt", "r").read().splitlines()
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == start:
            startpos = (x, y)
        if char == end:
            endpos = (x, y)

print("Antwoord 1: {}".format(len(find_shortest(startpos, grid, endpos))-1))

shortest_distance = 10000
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "a":
            try:
                distance = len(find_shortest((x,y), grid, endpos)) - 1
                if distance < shortest_distance:
                    shortest_distance = distance
            except:
                pass

print("Antwoord 2: {}".format(shortest_distance))

