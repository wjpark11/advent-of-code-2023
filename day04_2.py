with open("day04_input.txt", "rt") as f:
    inputs = f.readlines()
    cards = [input.strip() for input in inputs]

cards = [card[10:].split(" | ") for card in cards]

cards = [
    [
        card[0].strip().replace("  ", " ").split(" "),
        card[1].strip().replace("  ", " ").split(" "),
    ]
    for card in cards
]

winning_card_nums = [len([num for num in card[1] if num in card[0]]) for card in cards]

card_counter = {f"{i}": 0 for i in range(1, len(cards) + 1)}


for i, card_num in enumerate(winning_card_nums):
    for idx in range(i + 2, i + 2 + card_num):
        card_counter[f"{idx}"] += 1
        card_counter[f"{idx}"] += card_counter[f"{i + 1}"]

sum = 0
for _, num in card_counter.items():
    sum += num

print(sum + len(cards))
