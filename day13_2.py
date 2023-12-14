with open("day13_input.txt", "rt") as f:
    inputs = f.readlines()

inputs = [input.strip() for input in inputs]

patterns = [[]]
pattern_index = 0
for line in inputs:
    if line == "":
        patterns.append([])
        pattern_index += 1
    else:
        patterns[pattern_index].append(line)


def get_diff_num(pattern1: list | str, pattern2: list | str) -> int:
    diff_num = 0
    for item in zip(pattern1, pattern2):
        if item[0] != item[1]:
            diff_num += 1
    return diff_num


def get_row_reflextion_num(pattern: list) -> int:
    height = len(pattern)
    for i in range(height - 1):
        up_index = i
        down_index = i + 1
        total_diff = 0
        while total_diff < 2:
            row_diff = get_diff_num(pattern[up_index], pattern[down_index])
            total_diff += row_diff
            if up_index == 0 or down_index == height - 1:
                if total_diff == 1:
                    return i + 1
                else:
                    break
            up_index -= 1
            down_index += 1
    return 0


def get_column_reflextion_num(pattern: list) -> int:
    width = len(pattern[0])
    for i in range(width - 1):
        left_index = i
        right_index = i + 1
        total_diff = 0
        while total_diff < 2:
            column_diff = get_diff_num(
                [line[left_index] for line in pattern],
                [line[right_index] for line in pattern],
            )
            total_diff += column_diff
            if left_index == 0 or right_index == width - 1:
                if total_diff == 1:
                    return i + 1
                else:
                    break
            left_index -= 1
            right_index += 1
    return 0


total = 0
for pattern in patterns:
    total += get_row_reflextion_num(pattern) * 100 + get_column_reflextion_num(pattern)

print(total)
