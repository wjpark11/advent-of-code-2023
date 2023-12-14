import re


with open("day14_input.txt", "rt") as f:
    inputs = [line.strip() for line in f.readlines()]

platform = inputs


def get_right_tilted_row(row: str) -> str:
    row_chuncks = re.findall(r"([O\.]*#|[O\.]*$)", row)
    tilted_row = ""
    for chunck in row_chuncks:
        num_dots = chunck.count(".")
        num_round_rocks = chunck.count("O")
        cube_rock = "#" if chunck.endswith("#") else ""
        tilted_row += "." * num_dots + "O" * num_round_rocks + cube_rock
    return tilted_row


WIDTH = len(platform[0])
HEIGHT = len(platform)

rotated_platform = []
for i in range(WIDTH):
    rotated_platform.append("".join([row[i] for row in platform[::-1]]))

tilted_platform = []
for row in rotated_platform:
    tilted_platform.append(get_right_tilted_row(row))


total_load = 0
for i in range(HEIGHT):
    total_load += [row[i] for row in tilted_platform].count("O") * (i + 1)

print(total_load)
