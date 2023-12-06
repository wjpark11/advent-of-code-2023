with open("day02_input.txt", "rt") as f:
    games = f.readlines()
    games = [game.strip() for game in games]


def get_cube_nums(cube_str: str) -> dict:
    cube_dict = {"red": 0, "green": 0, "blue": 0}
    for cube in cube_str.split(", "):
        num, color = cube.split(" ")
        cube_dict[color] += int(num)

    return cube_dict


def is_valid_list(cube_dict_list: list) -> bool:
    for cube_dict in cube_dict_list:
        if cube_dict["red"] > 12:
            return False
        if cube_dict["green"] > 13:
            return False
        if cube_dict["blue"] > 14:
            return False
    return True


sum = 0
for i, game in enumerate(games):
    cube_str = game.split(": ")[1]
    cube_str_list = cube_str.split("; ")
    cube_dict_list = [get_cube_nums(cube_str) for cube_str in cube_str_list]
    if is_valid_list(cube_dict_list):
        sum += i + 1

print(sum)
