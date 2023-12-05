from pathlib import Path


def read_input(basename: str, *, trailing_empty_row: bool = False):
    input_dir = Path(__file__).parent.parent / "inputs"
    input_file = input_dir / f"{basename}.txt"

    with input_file.open() as fp:
        rows = [row.strip() for row in fp]

    if trailing_empty_row and rows[-1] != "":
        rows.append("")

    return rows
