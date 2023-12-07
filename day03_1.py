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


symbol_positions = {
    (i, j)
    for i in range(HEIGHT)
    for j in range(WIDTH)
    if inputs[i][j] not in ".1234567890"
}

sum = 0
for i, input in enumerate(inputs):
    match_num_objs = re.finditer(r"(\d+)", input)
    for obj in match_num_objs:
        start_idx = obj.start()
        end_idx = obj.end() - 1
        adjacent_positions = set(get_adjacent_positions(i, start_idx, end_idx))
        if adjacent_positions.intersection(symbol_positions):
            sum += int(obj.group())

print(sum)
