from collections import OrderedDict
from utils import read_input


class Number:
    def __init__(self, digits):
        self.value = int("".join(digits))


# Figure out where numbers and symbols are
numbers = dict()
symbols = list()
gears = set()
for i, row in enumerate(read_input("Day03-Puzzle")):
    stack = OrderedDict()
    for j, c in enumerate(row + "."):
        if c.isdigit():
            stack[(i, j)] = c
        else:
            # Combine digits into a number and push to memory
            if len(stack) > 0:
                number = Number(stack.values())
                for ij in stack.keys():
                    numbers[ij] = number
                stack.clear()

            # Found a symbol?
            if c != ".":
                symbols.append((i, j))
            if c == "*":
                gears.add((i, j))

# Sum up numbers adjacent to symbols
part_numbers = set()
gear_ratios = list()
for i, j in symbols:
    neighbors = set()
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            ij = (i + di, j + dj)

            if ij in numbers:
                part_numbers.add(numbers[ij])
                neighbors.add(numbers[ij])

    # Is this a gear?
    if (i, j) in gears and len(neighbors) == 2:
        n = list(neighbors)
        gear_ratios.append(n[0].value * n[1].value)

print(f"Solution 1: {sum(num.value for num in part_numbers)}")
print(f"Solution 2: {sum(gear_ratios)}")
