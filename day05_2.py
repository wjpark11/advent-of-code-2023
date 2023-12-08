with open("day05_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]


seed_ranges = [int(seed) for seed in inputs.pop(0).split(" ")[1:]]
seed_ranges = [range(i, i + j) for i, j in zip(seed_ranges[::2], seed_ranges[1::2])]

print(seed_ranges)


maps = dict()

map_name = ""
for line in inputs:
    if line.endswith(":"):
        map_name = line[:-1]
        maps[map_name] = []
    elif line == "":
        pass
    else:
        maps[map_name].append([int(num) for num in line.split(" ")])


def get_mapped_value(input_val: int, map_list: list) -> int:
    for map in map_list:
        if input_val in range(map[1], map[1] + map[2]):
            return input_val - map[1] + map[0]
    return input_val


location_nums = []

for seed in seed_ranges[0]:
    for _, map_list in maps.items():
        seed = get_mapped_value(seed, map_list)
    location_nums.append(seed)

print(min(location_nums))
