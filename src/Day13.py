import numpy as np

from utils import read_input


def block_to_array(block):
    return np.array([[1 if c == "#" else 0 for c in row] for row in block], dtype=bool)


def read_input_as_arrays(filename):
    arrays = []

    block = []
    for row in read_input(filename, trailing_empty_row=True):
        if len(row) == 0:
            arrays.append(block_to_array(block))
            block = []
        else:
            block.append(row)

    return arrays


def compare_blocks(block1, block2, *, allow_smudge=False):
    if not allow_smudge:
        return np.array_equal(block1, block2)
    else:
        return np.count_nonzero(block1 != block2) == 1


def find_mirror_plane(block, allow_smudge):
    for i in range(1, block.shape[0]):
        mirrored = np.flip(block[:i, :], axis=0)
        remainder = block[i:, :]

        if mirrored.shape[0] > remainder.shape[0]:
            mirrored = mirrored[: remainder.shape[0], :]
        else:
            remainder = remainder[: mirrored.shape[0], :]

        if compare_blocks(mirrored, remainder, allow_smudge=allow_smudge):
            return 100 * i

    for i in range(1, block.shape[1]):
        mirrored = np.flip(block[:, :i], axis=1)
        remainder = block[:, i:]

        if mirrored.shape[1] > remainder.shape[1]:
            mirrored = mirrored[:, : remainder.shape[1]]
        else:
            remainder = remainder[:, : mirrored.shape[1]]

        if compare_blocks(mirrored, remainder, allow_smudge=allow_smudge):
            return i

    raise ValueError("No mirror plane found")


if __name__ == "__main__":
    blocks = read_input_as_arrays("Day13-Puzzle")
    print(f"Solution 1: {sum(find_mirror_plane(block, False) for block in blocks)}")
    print(f"Solution 2: {sum(find_mirror_plane(block, True) for block in blocks)}")
