terminal_output = open("input.txt", "r").read().splitlines()

sum100k = 0

class Node:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.nodes = {}

    def addNode(self, node):
        self.nodes[node.name] = node

    def containsNode(self, name):
        return name in self.nodes.keys()

    def getSize(self):
        total_size = 0
        for node in self.nodes:
            total_size += self.nodes[node].getSize()
        return self.size + total_size 

def find100k(node):
    global sum100k
    if node.size == 0:
        if node.getSize() < 100000:
            sum100k += node.getSize()
            print("dir: {} - size: {}".format(node.name, node.getSize()))
    for child in node.nodes:
        find100k(node.nodes[child])

def findClosestTo(node, size):
    global wantedNode
    if node.getSize() > size and node.getSize() < wantedNode.getSize():
        print("Nieuwe closest: {} - {}".format(node.name, node.getSize()))
        wantedNode = node

    for child in node.nodes:
        findClosestTo(node.nodes[child], size)

root = Node("/", 0, "")
current_dir = root
wantedNode = root

index = 0
while (index < len(terminal_output)):
    command = terminal_output[index]
    print(command)
    if command == "$ cd /":
        current_dir = root
        index += 1
        continue
    if command == "$ cd ..":
        current_dir = current_dir.parent
        index += 1
        continue
    if command[0:4] == "$ cd":
        new_dir = command[5:]
        if not current_dir.containsNode(new_dir):
            new_node = Node(new_dir, 0, current_dir)
            current_dir.addNode(new_node)
        current_dir = current_dir.nodes[new_dir]
        index += 1
        continue
    if command == "$ ls":
        while(not terminal_output[index+1][0] == "$"):
            index += 1
            (size, name) = terminal_output[index].split(" ")
            if size == "dir":
                size = "0"
            if not current_dir.containsNode(name):
                new_node = Node(name, int(size), current_dir)
                current_dir.addNode(new_node)
        index +=1
        continue
    break

find100k(root)
print(sum100k)        

print("Free space = {}".format(70000000 - root.getSize()))
print("Needed to freeup is: {}".format(30000000 - (70000000 - root.getSize())))

findClosestTo(root, 6132864)