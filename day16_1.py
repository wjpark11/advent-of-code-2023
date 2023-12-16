with open("day16_input.txt", "rt") as f:
    contraption = [line.strip() for line in open("day16_input.txt", "rt")]

energized = {
    (0, 0),
}
initial_beam = (0, 0, "R")
all_beams = {
    initial_beam,
}


def get_next_beam(beam: tuple) -> list[tuple]:
    i, j, direction = beam
    mirror = contraption[i][j]

    if mirror == ".":
        if direction == "R":
            beams = [(i, j + 1, "R")]
        elif direction == "L":
            beams = [(i, j - 1, "L")]
        elif direction == "U":
            beams = [(i - 1, j, "U")]
        elif direction == "D":
            beams = [(i + 1, j, "D")]
    elif mirror == "/":
        if direction == "R":
            beams = [(i - 1, j, "U")]
        elif direction == "L":
            beams = [(i + 1, j, "D")]
        elif direction == "U":
            beams = [(i, j + 1, "R")]
        elif direction == "D":
            beams = [(i, j - 1, "L")]
    elif mirror == "\\":
        if direction == "R":
            beams = [(i + 1, j, "D")]
        elif direction == "L":
            beams = [(i - 1, j, "U")]
        elif direction == "U":
            beams = [(i, j - 1, "L")]
        elif direction == "D":
            beams = [(i, j + 1, "R")]
    elif mirror == "-":
        if direction == "R":
            beams = [(i, j + 1, "R")]
        elif direction == "L":
            beams = [(i, j - 1, "L")]
        elif direction == "U":
            beams = [(i, j - 1, "L"), (i, j + 1, "R")]
        elif direction == "D":
            beams = [(i, j - 1, "L"), (i, j + 1, "R")]
    elif mirror == "|":
        if direction == "R":
            beams = [(i + 1, j, "D"), (i - 1, j, "U")]
        elif direction == "L":
            beams = [(i + 1, j, "D"), (i - 1, j, "U")]
        elif direction == "U":
            beams = [(i - 1, j, "U")]
        elif direction == "D":
            beams = [(i + 1, j, "D")]

    return set(
        filter(
            lambda x: x[0] >= 0
            and x[1] >= 0
            and x[0] < len(contraption)
            and x[1] < len(contraption[0]),
            beams,
        )
    )


next_beams = get_next_beam(initial_beam)
for position in [(beam[0], beam[1]) for beam in next_beams]:
    energized.add(position)

while True:
    new_beams = set()
    for beam in next_beams:
        new_beams = new_beams.union(get_next_beam(beam))

    # print(new_beams)
    if len(new_beams) == 0:
        break
    else:
        next_beams = new_beams.difference(all_beams)
        all_beams = all_beams.union(new_beams)
        for position in [(beam[0], beam[1]) for beam in next_beams]:
            energized.add(position)

print(len(energized))
