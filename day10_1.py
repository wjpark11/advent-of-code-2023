with open("day10_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

board = [list(line) for line in inputs]
WIDTH = len(board[0])
HEIGHT = len(board)

for i, line in enumerate(board):
    if "S" in line:
        START = (i, line.index("S"))
        break


CONVERTER = {
    "|": "UD",
    "-": "LR",
    "L": "UR",
    "J": "UL",
    "7": "DL",
    "F": "DR",
    ".": ".",
    "S": "S",
}

board = [[CONVERTER[board[i][j]] for j in range(WIDTH)] for i in range(HEIGHT)]


def get_next_position(position: tuple, direction: str) -> tuple:
    (i, j) = position
    if i != 0 and direction == "U":
        return (i - 1, j)
    elif i != HEIGHT - 1 and direction == "D":
        return (i + 1, j)
    elif j != 0 and direction == "L":
        return (i, j - 1)
    elif j != WIDTH - 1 and direction == "R":
        return (i, j + 1)


converted_direction = {
    "D": "U",
    "U": "D",
    "L": "R",
    "R": "L",
}


def find_loop(board: list, start: tuple) -> list:
    path = [start]
    (i, j) = start
    if i != 0 and "D" in board[i - 1][j]:
        direction, next_position = "U", (i - 1, j)
    elif i != HEIGHT - 1 and "U" in board[i + 1][j]:
        direction, next_position = "D", (i + 1, j)
    elif j != 0 and "R" in board[i][j - 1]:
        direction, next_position = "L", (i, j - 1)
    else:
        direction, next_position = "R", (i, j + 1)

    while next_position not in path:
        path.append(next_position)
        direction = board[next_position[0]][next_position[1]].replace(
            converted_direction[direction], ""
        )
        next_position = get_next_position(next_position, direction)

    return path


print(len(find_loop(board, START)) / 2)
