import re

with open("day03_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

WIDTH = len(inputs[0])
HEIGHT = len(inputs)


def get_adjacent_positions(row_idx: int, start_idx: int, end_idx: int) -> list:
    """
    Returns a list of adjacent positions to the given position.
    """
    adjacent_positions = []
    if row_idx > 0:
        for i in range(max(0, start_idx - 1), min(end_idx + 1, WIDTH - 1) + 1):
            adjacent_positions.append((row_idx - 1, i))
    if row_idx < HEIGHT - 1:
        for i in range(max(0, start_idx - 1), min(end_idx + 1, WIDTH - 1) + 1):
            adjacent_positions.append((row_idx + 1, i))
    if start_idx > 0:
        adjacent_positions.append((row_idx, start_idx - 1))
    if end_idx < WIDTH - 1:
        adjacent_positions.append((row_idx, end_idx + 1))
    return adjacent_positions


star_positions = {
    (i, j) for i in range(HEIGHT) for j in range(WIDTH) if inputs[i][j] == "*"
}

part_nums = set()

for i, input in enumerate(inputs):
    match_num_objs = re.finditer(r"(\d+)", input)
    for obj in match_num_objs:
        start_idx = obj.start()
        end_idx = obj.end() - 1
        num = int(obj.group())
        part_nums.add((num, tuple(get_adjacent_positions(i, start_idx, end_idx))))

sum = 0
for star_position in star_positions:
    adj_count = 0
    ratio = 1
    for part_num in part_nums:
        if star_position in part_num[1]:
            adj_count += 1
            ratio *= part_num[0]
    if adj_count == 2:
        sum += ratio

print(sum)
