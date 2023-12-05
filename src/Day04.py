import re

from utils import read_input


def extract_numbers(string):
    for v in re.split(r"\s+", string.strip()):
        yield int(v)


rows = read_input("Day04-Puzzle")

points = 0
cards = [1] * len(rows)
for i, row in enumerate(rows):
    parts = re.match(r"Card\s+\d+\:\s+((?:\d+\s+)+)\|\s+((?:\d+\s*)+)$", row)
    winning = set(extract_numbers(parts.group(1)))
    drawn = list(extract_numbers(parts.group(2)))

    # Compute number of points scored with this card
    matches = sum(1 for draw in drawn if draw in winning)
    if matches > 0:
        points += 2 ** (matches - 1)

    # Compute number of additional cards won with this card
    for j in range(matches):
        cards[i + j + 1] += cards[i]

print(f"Solution 1: {points}")
print(f"Solution 2: {sum(cards)}")
