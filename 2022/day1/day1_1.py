f = open("input1.txt", "r")
index = 0
elfs = [0]
for x in f:
  if x.strip() == "":
    index = index + 1
    elfs.append(0)
  else:
    elfs[index] = elfs[index] + int(x.strip())

elfs.sort(reverse=True)
print("Answer 1: " + str(elfs[0]))
print("Answer 2: " + str(elfs[0] + elfs[1] + elfs[2]))