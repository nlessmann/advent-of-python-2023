import re
import math

from utils import read_input


def extract_integers(s, part):
    if part == 1:
        return [int(v) for v in re.findall(r"\d+", s)]
    else:
        return [int("".join(re.findall(r"\d", s)))]


# Parse input
rows = read_input("Day06-Puzzle")
for part in (1, 2):
    times = extract_integers(rows[0], part)
    records = extract_integers(rows[1], part)

    # Simulate races
    score = None
    for time, record in zip(times, records):
        # Take equation distance = (time - charge) * charge
        # Set distance = record, solve for charge
        first_wtw = math.ceil(0.5 * (time - math.sqrt(time**2 - 4 * record)))
        last_wtw = math.floor(0.5 * (time + math.sqrt(time**2 - 4 * record)))
        ways_to_win = last_wtw - first_wtw + 1

        score = ways_to_win if score is None else score * ways_to_win

    print(f"Solution {part}: {score}")
