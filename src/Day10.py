import numpy as np

from utils import read_input


class Tiles:
    TYPES = {
        "GROUND": (0, "."),
        "START": (1, "S"),
        "PIPE_NS": (2, "|"),
        "PIPE_EW": (3, "-"),
        "PIPE_NE": (4, "L"),
        "PIPE_NW": (5, "J"),
        "PIPE_SW": (6, "7"),
        "PIPE_SE": (7, "F"),
    }

    FLOW = [
        None,
        {(-1, 0), (1, 0), (0, -1), (0, 1)},
        {(-1, 0), (1, 0)},
        {(0, -1), (0, 1)},
        {(-1, 0), (0, 1)},
        {(-1, 0), (0, -1)},
        {(1, 0), (0, -1)},
        {(1, 0), (0, 1)},
    ]

    def __init__(self, rows):
        # Create grid of integers
        grid = []
        lut = {s[1]: s[0] for s in self.TYPES.values()}
        for row in rows:
            grid.append([lut[c] for c in row])

        self.grid = np.array(grid)

        # Make sure type names are available as instance members
        for k, s in self.TYPES.items():
            setattr(self, k, s[0])

    def __getitem__(self, xy):
        x, y = xy
        if x < 0 or x >= self.grid.shape[0] or y < 0 or y >= self.grid.shape[1]:
            return self.GROUND
        else:
            return self.grid[x, y]

    def find_start(self):
        c = np.where(self.grid == self.START)
        return c[0].item(), c[1].item()

    def find_possible_steps(self, xy):
        x, y = xy

        # Determine the type of pipe at this position and the corresponding
        # flow directions
        pipe = self.grid[x, y]
        flow = self.FLOW[pipe]

        # Check north, south, west and east
        steps = []
        if (-1, 0) in flow and self[x - 1, y] in (
            self.PIPE_NS,
            self.PIPE_SW,
            self.PIPE_SE,
        ):
            steps.append((x - 1, y))
        if (1, 0) in flow and self[x + 1, y] in (
            self.PIPE_NS,
            self.PIPE_NW,
            self.PIPE_NE,
        ):
            steps.append((x + 1, y))
        if (0, -1) in flow and self[x, y - 1] in (
            self.PIPE_EW,
            self.PIPE_NE,
            self.PIPE_SE,
        ):
            steps.append((x, y - 1))
        if (0, 1) in flow and self[x, y + 1] in (
            self.PIPE_EW,
            self.PIPE_NW,
            self.PIPE_SW,
        ):
            steps.append((x, y + 1))

        return steps


if __name__ == "__main__":
    tiles = Tiles(read_input("Day10-Puzzle"))
    start = tiles.find_start()

    steps = tiles.find_possible_steps(start)
    path = [start]
    while len(steps) > 0:
        path.append(steps[0])
        steps = [
            step for step in tiles.find_possible_steps(path[-1]) if step not in path
        ]

    print(f"Solution 1: {len(path) // 2}")

    # Shoelace formula to calculate area
    area = 0
    for i in range(len(path)):
        if i == 0:
            prev = path[-1]
        else:
            prev = path[i - 1]
        curr = path[i]

        area += prev[0] * curr[1] - prev[1] * curr[0]
    area = abs(area / 2)

    # Pick's theorem to calculate integer points inside
    # A = i + b/2 - 1
    # i = A - b/2 + 1
    print(f"Solution 2: {int(area - len(path) / 2 + 1)}")
