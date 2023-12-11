with open("day11_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

# galaxy = [[char for char in line] for line in inputs]
galaxy = inputs

empty_row_indexes = [
    i for i, row in enumerate(galaxy) if all([char == "." for char in row])
]
empty_col_indexes = [
    i for i in range(len(galaxy[0])) if all([row[i] == "." for row in galaxy])
]


def distance(x: tuple, y: tuple) -> int:
    x_range = range(x[0], y[0] + 1) if x[0] < y[0] else range(y[0], x[0] + 1)
    y_range = range(x[1], y[1] + 1) if x[1] < y[1] else range(y[1], x[1] + 1)
    double_cnt_x = len([x for x in empty_row_indexes if x in x_range])
    double_cnt_y = len([y for y in empty_col_indexes if y in y_range])
    dist = abs(x[0] - y[0]) + abs(x[1] - y[1]) + double_cnt_x + double_cnt_y
    return dist

stars = [(i, j) for i, row in enumerate(galaxy) for j, char in enumerate(row) if char == "#"]

distances = []
for star in stars:
    for other_star in stars:
        distances.append(distance(star, other_star))

print(sum(distances)/2)