with open("day15_input.txt", "rt") as f:
    inputs = f.readline().split(",")


def get_hash(string: str) -> int:
    current_val = 0
    for char in string:
        current_val += ord(char)
        current_val *= 17
        current_val %= 256

    return current_val


sum_of_hash = 0
for string in inputs:
    sum_of_hash += get_hash(string)

print(sum_of_hash)
