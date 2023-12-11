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
    pass
