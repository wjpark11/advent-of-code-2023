import re

with open("day15_input.txt", "rt") as f:
    inputs = f.readline().split(",")

operations = [re.match(r"(\w+)(-|=)(\d*)", input).groups() for input in inputs]

boxes = [{"box_num": i, "lens": {"name": [], "focal_len": []}} for i in range(256)]


def get_hash(string: str) -> int:
    current_val = 0
    for char in string:
        current_val += ord(char)
        current_val *= 17
        current_val %= 256

    return current_val


for op in operations:
    box_num = get_hash(op[0])
    if op[1] == "-":
        if op[0] in boxes[box_num]["lens"]["name"]:
            lens_index = boxes[box_num]["lens"]["name"].index(op[0])
            boxes[box_num]["lens"]["name"].pop(lens_index)
            boxes[box_num]["lens"]["focal_len"].pop(lens_index)
    elif op[1] == "=":
        if op[0] not in boxes[box_num]["lens"]["name"]:
            boxes[box_num]["lens"]["name"].append(op[0])
            boxes[box_num]["lens"]["focal_len"].append(int(op[2]))
        else:
            lens_index = boxes[box_num]["lens"]["name"].index(op[0])
            boxes[box_num]["lens"]["focal_len"][lens_index] = int(op[2])


focusing_power = 0
for box in boxes:
    box_index = box["box_num"]
    for i, length in enumerate(box["lens"]["focal_len"]):
        focusing_power += (box_index + 1) * (i + 1) * length

print(focusing_power)
