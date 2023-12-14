import re


with open("day14_input.txt", "rt") as f:
    inputs = [line.strip() for line in f.readlines()]

platform = inputs


def rotate_platform(platform: list) -> list:
    width = len(platform[0])
    rotated_platform = []
    for i in range(width):
        rotated_platform.append("".join([row[i] for row in platform[::-1]]))
    return rotated_platform


def unrotate_platform(platform: list) -> list:
    width = len(platform[0])
    height = len(platform)
    unrotated_platform = []
    for i in range(width):
        unrotated_platform.append("".join([row[height - i - 1] for row in platform]))
    return unrotated_platform


def get_right_tilted_row(row: str) -> str:
    row_chuncks = re.findall(r"([O\.]*#|[O\.]*$)", row)
    tilted_row = ""
    for chunck in row_chuncks:
        num_dots = chunck.count(".")
        num_round_rocks = chunck.count("O")
        cube_rock = "#" if chunck.endswith("#") else ""
        tilted_row += "." * num_dots + "O" * num_round_rocks + cube_rock
    return tilted_row


def tilt_right(platform: list) -> list:
    tilted_platform = []
    for row in platform:
        tilted_platform.append(get_right_tilted_row(row))
    return tilted_platform


def tilt_cycle(platform: list) -> list:
    north_tilted = unrotate_platform(tilt_right(rotate_platform(platform)))
    west_tilted = unrotate_platform(
        unrotate_platform(tilt_right(rotate_platform(rotate_platform(north_tilted))))
    )
    south_tilted = rotate_platform(tilt_right(unrotate_platform(west_tilted)))
    east_tilted = tilt_right(south_tilted)

    return east_tilted


cycled_platforms = []

while True:
    cycled_platforms.append(platform)
    platform = tilt_cycle(platform)
    if platform in cycled_platforms:
        first_duplicate_index = cycled_platforms.index(platform)
        break

unrepeated_cylcle_length = first_duplicate_index
repeated_cycle_length = len(cycled_platforms) - first_duplicate_index
remainder = (1000000000 - first_duplicate_index) % repeated_cycle_length

final_platform = cycled_platforms[first_duplicate_index + remainder]

final_total_load = 0
HEIGHT = len(final_platform)
for i, row in enumerate(final_platform):
    final_total_load += row.count("O") * (HEIGHT - i)

print(final_total_load)
