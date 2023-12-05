import re

with open("day01_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

DIGITS = {
    "two": 2,
    "one": 1,
    "seven": 7,
    "nine": 9,
    "three": 3,
    "five": 5,
    "eight": 8,
    "four": 4,
    "six": 6,
}


def convert_to_digits(line: str) -> str:
    while re.search(r"(two|one|seven|nine|three|five|eight|four|six)", line):
        for i, _ in enumerate(line):
            if re.match(r"(two|one|seven|nine|three|five|eight|four|six)", line[i:]):
                digit = re.match(r"(two|one|seven|nine|three|five|eight|four|six)", line[i:]).group(1)
                line = line.replace(digit, str(DIGITS[digit]), 1)
                break
    return line


converted_inputs = []
for line in inputs:
    converted_inputs.append(convert_to_digits(line))

calibration_value_sum = 0
for line in converted_inputs:
    nums = [num for num in line if num in "0123456789"]
    calibration_value = int(nums[0] + nums[-1])
    calibration_value_sum += calibration_value

print(calibration_value_sum)
print(convert_to_digits("twoneightwo"))
