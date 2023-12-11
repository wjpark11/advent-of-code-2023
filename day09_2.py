with open("day09_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

sequences = [list(map(int, line.split(" "))) for line in inputs]


def get_extrapolated_value(sequence: list[int]) -> int:
    sequences = [sequence]
    while True:
        new_sequence = [
            sequences[-1][i + 1] - sequences[-1][i]
            for i in range(len(sequences[-1]) - 1)
        ]
        sequences.append(new_sequence)
        if all(map(lambda x: x == 0, new_sequence)):
            break

    return sum([seq[0] for seq in sequences[::2]]) - sum(
        [seq[0] for seq in sequences[1::2]]
    )


sum = sum([get_extrapolated_value(sequence) for sequence in sequences])
print(sum)
