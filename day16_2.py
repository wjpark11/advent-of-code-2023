with open("day16_input.txt", "rt") as f:
    contraption = [line.strip() for line in open("day16_input.txt", "rt")]


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


def get_energized_tile_num(initial_beam: tuple) -> int:
    next_beams = get_next_beam(initial_beam)
    energized = {
        (initial_beam[0], initial_beam[1]),
    }
    all_beams = {
        initial_beam,
    }
    for position in [(beam[0], beam[1]) for beam in next_beams]:
        energized.add(position)

    while True:
        new_beams = set()
        for beam in next_beams:
            new_beams = new_beams.union(get_next_beam(beam))

        if len(new_beams) == 0:
            break
        else:
            next_beams = new_beams.difference(all_beams)
            all_beams = all_beams.union(new_beams)
            for position in [(beam[0], beam[1]) for beam in next_beams]:
                energized.add(position)

    return len(energized)


max_energized = 0
possible_initial_beams = (
    [(0, i, "D") for i in range(len(contraption))]
    + [(len(contraption[0]) - 1, i, "U") for i in range(len(contraption))]
    + [(j, 0, "R") for j in range(len(contraption[0]))]
    + [(j, len(contraption) - 1, "L") for j in range(len(contraption[0]))]
)

for initial_beam in possible_initial_beams:
    max_energized = max(max_energized, get_energized_tile_num(initial_beam))

print(max_energized)