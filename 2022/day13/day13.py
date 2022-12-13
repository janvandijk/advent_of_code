import functools

input = open("input.txt", "r").read().split("\n\n")

incorrect, unknown, correct = -1, 0, 1
def correctOrder(left,right):
    # print("- Compare {} vs {}".format(left,right))
    if type(left) is list and type(right) is list:
#        print("both list: {} and {}".format(left,right))
        for index, item in enumerate(left):
            # print("{} - {} = len {}".format(index,item, len(right)))
            if len(right) - 1 < index:
                # print("Right ran out of items - incorrect")
                return incorrect
#            print("Index: {} - left {} - right {}".format(index,item,right[index]))
            result = correctOrder(left[index], right[index])
            if result in [incorrect,correct]:
                return result
        if (len(left) < len(right)):
            # print("Left ran out of items - correct")
            return correct
        return unknown
    if type(left) is int and type(right) is int:
#        print("{} < {} = {}".format(left, right, left<right))
        if left < right:
#            print("correct")
            return correct
        if left > right:
#            print("incorrect")
            return incorrect
#        print("unknown")
        return unknown

    if type(left) is list:
#        print("left is list")
        return correctOrder(left, [right])
    else:
#        print("right is list")
        return correctOrder([left], right)

sum = 0
for i, packet in enumerate(input):
    a,b = packet.splitlines()
    left = eval(a)
    right = eval(b)

    if correctOrder(left,right) == correct:
        sum += i + 1

print(f"Antwoord 1: {sum}")

all_items = []
for i, packet in enumerate(input):
    a,b = packet.splitlines()
    all_items.append(a)
    all_items.append(b)

all_items.append("[[2]]")
all_items.append("[[6]]")

def compare(x, y):
    return -correctOrder(eval(x),eval(y))

sorted_l = sorted(all_items, key=functools.cmp_to_key(compare))
a = sorted_l.index("[[2]]")
b = sorted_l.index("[[6]]")

print(f"Antwoord 2: {a*b}")
