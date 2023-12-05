import re

from utils import read_input


class Range:
    def __init__(self, start: int, length: int):
        self.first = start
        self.last = start + length - 1
        self.length = length

    def contains(self, value: int) -> bool:
        return value >= self.first and value < self.first + self.length


class CatToCatRange:
    def __init__(self, src_start: int, dst_start: int, length: int):
        self.src_range = Range(src_start, length)
        self.dst_range = Range(dst_start, length)

    def contains(self, src: int) -> bool:
        return self.src_range.contains(src)

    def translate(self, src: int) -> int:
        offset = src - self.src_range.first
        return self.dst_range.first + offset


class CatToCatMap:
    def __init__(self, rows):
        # Extract names of source and destination category
        m = re.match("([a-z]+)-to-([a-z]+)", rows[0])
        self.source = m.group(1)
        self.destination = m.group(2)

        # Extract ranges
        self.ranges = []
        for row in rows[1:]:
            m = [int(v) for v in re.findall(r"\d+", row)]
            self.ranges.append(CatToCatRange(m[1], m[0], m[2]))

    def translate(self, src: int) -> int:
        for range in self.ranges:
            if range.contains(src):
                return range.translate(src)

        return src


# Parse input
seeds = []
maps = {}
rows = []
for row in read_input("Day05-Puzzle", trailing_empty_row=True):
    if len(seeds) == 0:
        seeds = [int(v) for v in re.findall(r"\d+", row)]
    elif row == "":
        if len(rows) > 0:
            c2c = CatToCatMap(rows)
            maps[c2c.source] = c2c
            rows.clear()
    else:
        rows.append(row)

# Translate seed categories into location categories
category = "seed"
values = list(seeds)
while category != "location":
    lut = maps[category]
    values = [lut.translate(value) for value in values]
    category = lut.destination

print(f"Solution 1: {min(values)}")

# Seeds are ranges actually
ranges = []
for i in range(0, len(seeds), 2):
    ranges.append(Range(seeds[i], seeds[i + 1]))

category = "seed"
while category != "location":
    lut = maps[category]

    new_ranges = []
    for value_range in ranges:
        knots = {value_range.first, value_range.last}
        for lut_range in lut.ranges:
            knots.add(lut_range.src_range.first)
            knots.add(lut_range.src_range.last)

        knots = list(sorted(knots))
        while not value_range.contains(knots[0]):
            knots = knots[1:]
        while not value_range.contains(knots[-1]):
            knots = knots[:-1]

        for i in range(len(knots) - 1):
            new_ranges.append(
                Range(lut.translate(knots[i]), knots[i + 1] - knots[i] + 1)
            )

    ranges = new_ranges
    category = lut.destination

print(f"Solution 2: {min(range.first for range in ranges)}")
