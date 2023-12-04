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


def convert_to_digits(line):
    pass


converted_inputs = []
for line in inputs:
    line = convert_to_digits(line)
    converted_inputs.append(line)

sum = 0
for line in converted_inputs:
    nums = [num for num in line if num in "0123456789"]
    calibration_value = int(nums[0] + nums[-1])
    sum += calibration_value

print(sum)
