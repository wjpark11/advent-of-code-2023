with open("day09_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

sequences = [list(map(int, line.split(" "))) for line in inputs]

def get_extrapolated_value(sequence: list[int]) -> int:
    sequences = [sequence]
    