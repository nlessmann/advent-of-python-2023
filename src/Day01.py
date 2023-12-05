from utils import read_input


def sum_up_calibration_values(filename, lut):
    total = 0
    for row in read_input(filename):
        best_first = None
        best_last = None

        for i, digit in enumerate(lut):
            first_idx = row.find(digit)
            if first_idx >= 0 and (best_first is None or best_first[0] > first_idx):
                best_first = (first_idx, i % 10)

            last_idx = row.rfind(digit)
            if last_idx >= 0 and (best_last is None or best_last[0] < last_idx):
                best_last = (last_idx, i % 10)

        total += int(f"{best_first[1]}{best_last[1]}")

    return total


lut = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print(f"Part 1: {sum_up_calibration_values('Day01-Puzzle', lut)}")

lut += ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print(f"Part 2: {sum_up_calibration_values('Day01-Puzzle', lut)}")
