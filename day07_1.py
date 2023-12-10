from collections import Counter

with open("day07_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

cards = [input.split(" ") for input in inputs]
cards = [[card[0], int(card[1])] for card in cards]

CARD_INDEX = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.hand_type = self._hand_type()

    def _hand_type(self):
        hand_counter = Counter(self.cards)
        if len(hand_counter) == 1:
            return 7
        elif len(hand_counter) == 2:
            if hand_counter.most_common()[0][1] == 4:
                return 6
            else:
                return 5
        elif len(hand_counter) == 3:
            if hand_counter.most_common()[0][1] == 3:
                return 4
            else:
                return 3
        elif len(hand_counter) == 4:
            return 2
        else:
            return 1

    def __gt__(self, other):
        if self.hand_type == other.hand_type:
            for a, b in zip(self.cards, other.cards):
                if a != b:
                    return CARD_INDEX[a] > CARD_INDEX[b]
        else:
            return self.hand_type > other.hand_type

    def __str__(self):
        return str(self.cards)


hands = [Hand(card[0], card[1]) for card in cards]
hands.sort()

sum = 0
for i, hand in enumerate(hands):
    sum += hand.bid * (i + 1)

print(sum)
