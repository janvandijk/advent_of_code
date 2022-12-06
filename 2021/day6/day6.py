# 3,4,3,1,2
days = [0,0,0,0,0,0,0,0,0]

f = open("input.txt", "r")
for x in f.read().split(","):
    days[int(x)] += 1

for x in range(1,257):
    aantal = days.pop(0)
    days[6] += aantal
    days.append(aantal)

    print(sum(days))
