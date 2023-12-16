with open("day08_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

INSTRUCTIONS = inputs.pop(0)

NODES = {line[:3]: (line[7:10], line[12:-1]) for line in inputs[1:]}

steps = 0

position = "AAA"

while position != "ZZZ":
    if INSTRUCTIONS[steps % len(INSTRUCTIONS)] == "R":
        idx = 1
    else:
        idx = 0
    steps += 1
    position = NODES[position][idx]

print(steps)
