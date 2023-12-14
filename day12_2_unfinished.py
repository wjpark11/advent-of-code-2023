import re
from itertools import combinations

with open("day12_input.txt", "rt") as f:
    inputs = f.readlines()

inputs = [input.strip().split(" ") for input in inputs]
conditions = [
    {
        "line": (input[0] + "?") * 4 + input[0],
        "counts": list(map(int, input[1].split(","))) * 5,
    }
    for input in inputs
]


def get_possible_arrangement_num(condition: dict) -> int:
    line_list = [char for char in condition["line"]]
    total_damaged = sum(condition["counts"])
    unsettled_indices = [i for i, char in enumerate(line_list) if char == "?"]
    unsettled_damaged_num = total_damaged - len(
        [char for char in condition["line"] if char == "#"]
    )

    combis = combinations(unsettled_indices, unsettled_damaged_num)
    print(len(list(combis)))

    num = 0
    for combi in combis:
        line_list_copy = line_list.copy()
        for i in list(combi):
            line_list_copy[i] = "#"
        line = "".join(line_list_copy)
        if (
            len([len(item) for item in re.findall(r"\#+", line)])
            == len(condition["counts"])
            and [len(item) for item in re.findall(r"\#+", line)] == condition["counts"]
        ):
            num += 1

    return num


ans = 0
for condition in conditions:
    print(condition)
    ans += get_possible_arrangement_num(condition)


print(ans)
