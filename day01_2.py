with open("day01_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

DIGITS = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def convert_to_digits(line: str) -> str:
    for digit in DIGITS.keys():
        line = line.replace(digit, DIGITS[digit])
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
