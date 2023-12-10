from math import lcm

with open("day08_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

INSTRUCTIONS = inputs.pop(0)

NODES = {line[:3] : (line[7:10], line[12:-1]) for line in inputs[1:]}

positions = [position for position in NODES.keys() if position.endswith("A")]


def get_steps(position: str) -> int:
    steps = 0
    while not position.endswith("Z"):
        if INSTRUCTIONS[steps % len(INSTRUCTIONS)] == "R":
            idx = 1
        else:
            idx = 0
        steps += 1
        position = NODES[position][idx]
    return steps


step_list = []

for start_position in positions:
    step_list.append(get_steps(start_position))

print(lcm(*step_list))