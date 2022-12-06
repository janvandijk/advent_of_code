f = open("input.txt", "r")

sum = 0

for x in f:
    sacks = x.strip()
    sack1 = slice(0,len(sacks)//2)
    sack2 = slice(len(sacks)//2, len(sacks))

    itemType = list(set(sacks[sack1]) & set(sacks[sack2]))[0]
    itemValue = ord(itemType) - 64
    if (itemValue < 27):
        itemValue += 26
    else:
        itemValue -= 32

    sum += itemValue

print("Sum is: " + str(sum))
