import re

from utils import read_input


def find_color(string, color) -> int:
    match = re.search(rf"(\d+) {color}", string)
    return 0 if match is None else int(match.group(1))


class Game:
    def __init__(self, row):
        parts = row.split(":")
        self.id = int(parts[0][5:])

        self.red = 0
        self.green = 0
        self.blue = 0
        for round in parts[1].strip().split("; "):
            self.red = max(self.red, find_color(round, "red"))
            self.green = max(self.green, find_color(round, "green"))
            self.blue = max(self.blue, find_color(round, "blue"))

    def power(self) -> int:
        return self.red * self.green * self.blue


games = [Game(row) for row in read_input("Day02-Puzzle")]
max_red, max_green, max_blue = 12, 13, 14

sum_ids = 0
for game in games:
    if game.red <= max_red and game.green <= max_green and game.blue <= max_blue:
        sum_ids += game.id
print(f"Solution 1: {sum_ids}")

sum_powers = sum(game.power() for game in games)
print(f"Solution 2: {sum_powers}")
