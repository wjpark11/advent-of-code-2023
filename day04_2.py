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

winning_card_nums = [len([num for num in card[1] if num in card[0]]) for card in cards]


print(winning_card_nums)
