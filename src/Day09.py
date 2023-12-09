import numpy as np

from utils import read_input


class Series:
    def __init__(self, values):
        self.values = np.asarray(values)

    def next_value(self):
        if np.all(self.values == 0):
            return 0
        else:
            s = Series(np.diff(self.values))
            return self.values[-1] + s.next_value()

    def previous_value(self):
        if np.all(self.values == 0):
            return 0
        else:
            s = Series(np.diff(self.values))
            return self.values[0] - s.previous_value()


if __name__ == "__main__":
    series = []
    for row in read_input("Day09-Puzzle"):
        series.append(Series([int(v) for v in row.split(" ")]))

    result = sum(s.next_value() for s in series)
    print(f"Solution 1: {result}")

    result = sum(s.previous_value() for s in series)
    print(f"Solution 2: {result}")
