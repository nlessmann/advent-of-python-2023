import numpy as np
import itertools

from utils import read_input


def read_image(filename):
    return np.array([[c == "#" for c in line] for line in read_input(filename)])


def compute_steps(image, expansion_factor):
    # Find rows and columns that are entirely empty
    empty_rows = np.all(image == 0, axis=1)
    empty_cols = np.all(image == 0, axis=0)

    # Find all galaxies
    galaxies = map(
        lambda g: np.array(
            [
                g[0] + expansion_factor * np.sum(empty_rows[: g[0]]),
                g[1] + expansion_factor * np.sum(empty_cols[: g[1]]),
            ]
        ),
        zip(*np.where(image)),
    )

    # Compute all distances
    steps = 0
    for g1, g2 in itertools.combinations(galaxies, 2):
        steps += int(np.linalg.norm(g1 - g2, ord=1))
    return steps


if __name__ == "__main__":
    image = read_image("Day11-Puzzle")
    print(f"Solution 1: {compute_steps(image, expansion_factor=1)}")
    print(f"Solution 2: {compute_steps(image, expansion_factor=1000000 - 1)}")
