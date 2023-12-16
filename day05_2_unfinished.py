from time import time

with open("day05_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]


seed_ranges = [int(seed) for seed in inputs.pop(0).split(" ")[1:]]
seed_ranges = [[i, i + j - 1] for i, j in zip(seed_ranges[::2], seed_ranges[1::2])]


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


def get_mapped_range_from_single_range(input_range: list[int], map: list) -> list:
    source_range = [map[1], map[1] + map[2] - 1]
    mapped_range = []
    if input_range[1] < source_range[0] or input_range[0] > source_range[1]:
        mapped_range.append(input_range)
        return mapped_range
    elif input_range[0] >= source_range[0] and input_range[1] <= source_range[1]:
        mapped_range.append(
            [input_range[0] - map[1] + map[0], input_range[1] - map[1] + map[0]]
        )
        return mapped_range
    elif input_range[0] >= source_range[0] and input_range[1] > source_range[1]:
        mapped_range.append(
            [input_range[0] - map[1] + map[0], source_range[1] - map[1] + map[0]]
        )
        mapped_range.append([source_range[1] + 1, input_range[1]])
        return mapped_range
    elif input_range[0] < source_range[0] and input_range[1] <= source_range[1]:
        mapped_range.append([input_range[0], source_range[0] - 1])
        mapped_range.append(
            [source_range[0] - map[1] + map[0], input_range[1] - map[1] + map[0]]
        )
        return mapped_range
    else:
        mapped_range.append([input_range[0], source_range[0] - 1])
        mapped_range.append(
            [source_range[0] - map[1] + map[0], source_range[1] - map[1] + map[0]]
        )
        mapped_range.append([source_range[1] + 1, input_range[1]])
        return mapped_range


def get_mapped_range(input_ranges: list, map: list[int]) -> list:
    range_list = []
    for input_range in input_ranges:
        range_list += get_mapped_range_from_single_range(input_range, map)
    return range_list


location_list = seed_ranges

for _, map_list in maps.items():
    intermidiate_list = []
    for map in map_list:
        intermidiate_list += get_mapped_range(location_list, map)
    location_list = intermidiate_list
    print(len(location_list))

min_val = min(location_list, key=lambda x: x[0])[0]

print(min_val)
