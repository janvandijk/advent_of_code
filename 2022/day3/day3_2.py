f = open("input.txt", "r")

sum = 0
count = 0

sets = []

for x in f:
    sets.append(set(x.strip()))
    count += 1

    if (count == 3):
        itemType = list(sets[0] & sets[1] & sets[2])[0]

        itemValue = ord(itemType) - 64
        if (itemValue < 27):
            itemValue += 26
        else:
            itemValue -= 32

        sum += itemValue


        count = 0
        sets = []

print("Sum is: " + str(sum))
