import re

from functools import lru_cache
from utils import read_input


@lru_cache
def number_of_arrangements(springs, groups):
    if len(groups) == 0:
        # No more groups left, so the rest of the springs must be functioning
        return 1 if len(springs) == 0 or all(c in (".", "?") for c in springs) else 0

    # Get the first group
    springs_this_group, groups = groups[0], groups[1:]
    springs_other_groups = sum(groups) + len(groups)

    # Iterate over all possible start positions
    max_group_start = len(springs) - springs_other_groups - springs_this_group + 1
    first_damaged_spring = springs.find("#")
    if first_damaged_spring >= 0:
        max_group_start = min(max_group_start, first_damaged_spring + 1)

    arrangements = 0
    for i in range(max_group_start):
        j = i + springs_this_group
        if j <= len(springs) and "." not in springs[i:j]:
            if j < len(springs) and springs[j] == "#":
                continue

            arrangements += number_of_arrangements(springs[j + 1 :], groups)

    return arrangements


if __name__ == "__main__":
    result1 = 0
    result2 = 0
    for row in read_input("Day12-Puzzle"):
        parts = row.split(" ")

        springs = parts[0]
        groups = [int(g) for g in re.findall(r"\d+", parts[1])]
        result1 += number_of_arrangements(springs, tuple(groups))

        springs = "?".join([springs] * 5)
        groups = groups * 5
        result2 += number_of_arrangements(springs, tuple(groups))

    print(f"Solution 1: {result1}")
    print(f"Solution 2: {result2}")
