import re
import sys
from dataclasses import dataclass
import math

all_monkeys = {}
modulo = 0

@dataclass
class Monkey:
    id: int
    items: []
    operation: []
    test_divisible: int
    true_monkey: int
    false_monkey: int
    number_of_inspects = 0

    def inspect_items(self):
        while(len(self.items)>0):
            self.number_of_inspects +=1
            item = self.items.pop(0)
            value = item if self.operation[1] == "old" else int(self.operation[1])
            if self.operation[0] == "+":
                item += value
            if self.operation[0] == "-":
                item -= value
            if self.operation[0] == "*":
                item *= value
            if self.operation[0] == "/":
                item /= value

            item %= modulo

            if item % self.test_divisible == 0:
                all_monkeys[self.true_monkey].items.append(item)
            else:
                all_monkeys[self.false_monkey].items.append(item)

input = open("input.txt", "r").read()
rex = "Monkey (\d+):\s+\D+(.*)\s+Operation: new = old (.*)\s+\D+(\d+)\D+(\d+)\D+(\d+)"
for m in re.finditer(rex, input):
    id = int(m.group(1))
    items = [int(x) for x in m.group(2).split(", ")]
    operation = m.group(3).split(" ")
    test_divisible = int(m.group(4))
    true_monkey = int(m.group(5))
    false_monkey = int(m.group(6))
    all_monkeys[id] = Monkey(id, items, operation, test_divisible, true_monkey, false_monkey)
    modulo = test_divisible if modulo == 0 else modulo * test_divisible


for i in range(10000):
    for index in all_monkeys:
        all_monkeys[index].inspect_items()

for m in all_monkeys:
    print(all_monkeys[m].number_of_inspects)

