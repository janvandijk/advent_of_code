import functools

incorrect, unknown, correct = -1, 0, 1
def correctOrder(left,right):
    if type(left) is list and type(right) is list:
        for index in range(len(left)):
            if len(right) - 1 < index:
                return incorrect
            result = correctOrder(left[index], right[index])
            if result in [incorrect, correct]:
                return result
        if (len(left) < len(right)):
            return correct
        return unknown
    if type(left) is int and type(right) is int:
        if left < right:
            return correct
        if left > right:
            return incorrect
        return unknown

    if type(left) is list:
        return correctOrder(left, [right])
    else:
        return correctOrder([left], right)

input = open("input.txt", "r").read().split("\n\n")
sum = 0
for i, packet in enumerate(input):
    a, b = packet.splitlines()
    if correctOrder(eval(a), eval(b)) == correct:
        sum += i + 1
print(f"Antwoord 1: {sum}")

divider_packets = ["[[2]]", "[[6]]"]
all_items = [line for line in open("input.txt", "r").read().splitlines() if line != ""] + divider_packets

def compare(x, y):
    return correctOrder(eval(x),eval(y))

sorted_l = sorted(all_items, key=functools.cmp_to_key(compare), reverse=True)
a = sorted_l.index(divider_packets[0]) + 1
b = sorted_l.index(divider_packets[1]) + 1

print(f"Antwoord 2: {a*b}")
