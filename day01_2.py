with open("inputs/day01_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

DIGITS = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

converted_inputs = []
for line in inputs:
    for digit in DIGITS.keys():
        if digit in line:
            line = line.replace(digit, str(DIGITS[digit]))
    converted_inputs.append(line)

sum = 0
for line in converted_inputs:
    nums = [num for num in line if num in "0123456789"]
    print(line)
    print(nums)
    calibration_value = int(nums[0] + nums[-1])
    sum += calibration_value

print(sum)
