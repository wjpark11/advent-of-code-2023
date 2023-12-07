with open("day04_input.txt", "rt") as f:
    inputs = f.readlines()
    cards = [input.strip() for input in inputs]

cards = [card[10:].split(" | ") for card in cards]

cards = [
    [
        card[0].strip().replace("  ", " ").split(" "),
        card[1].strip().replace("  ", " ").split(" ")
    ]
    for card in cards
]

winning_numbers_list = [[num for num in card[1] if num in card[0]] for card in cards]

winning_points = [
    2 ** (len(winning_numbers) - 1)
    for winning_numbers in winning_numbers_list
    if winning_numbers
]


print(sum(winning_points))
