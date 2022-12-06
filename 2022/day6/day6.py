message = open("input.txt", "r").read()
index = 0
marker_length = 4
while(True):
    marker = message[index:marker_length + index]
    if (len(set(marker)) == marker_length):
        break
    index += 1

print(index + marker_length)