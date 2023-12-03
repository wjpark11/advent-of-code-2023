with open("inputs/day01_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]


sum = 0
for line in inputs:
    nums = [num for num in line if num in "0123456789"]
    calibration_value = int(nums[0] + nums[-1])
    sum += calibration_value

print(sum)
