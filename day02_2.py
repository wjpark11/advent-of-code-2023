with open("day02_input.txt", "rt") as f:
    games = f.readlines()
    games = [game.strip() for game in games]


def get_cube_nums(cube_str: str) -> dict:
    cube_dict = {"red": 0, "green": 0, "blue": 0}
    for cube in cube_str.split(", "):
        num, color = cube.split(" ")
        cube_dict[color] += int(num)

    return cube_dict


sum = 0
for game in games:
    cube_str = game.split(": ")[1]
    cube_str_list = cube_str.split("; ")
    cube_dict_list = [get_cube_nums(cube_str) for cube_str in cube_str_list]
    final_cube_dict = {"red": 0, "green": 0, "blue": 0}
    for cube_dict in cube_dict_list:
        final_cube_dict["red"] = max(cube_dict["red"], final_cube_dict["red"])
        final_cube_dict["green"] = max(cube_dict["green"], final_cube_dict["green"])
        final_cube_dict["blue"] = max(cube_dict["blue"], final_cube_dict["blue"])
    sum += final_cube_dict["red"] * final_cube_dict["green"] * final_cube_dict["blue"]

print(sum)
