import numpy as np

from utils import read_input


class Card:
    ranks = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "X": 0,
    }

    def __init__(self, kind):
        self.kind = kind
        self.rank = self.ranks[kind]

    @property
    def joker(self) -> bool:
        return self.rank == 0


class Hand:
    def __init__(self, cards, bet, *, joker=False):
        self.cards = [Card("X" if joker and kind == "J" else kind) for kind in cards]
        self.bet = bet

        # Compute frequency of identical cards
        _, frequencies = np.unique(
            [card.kind for card in self.cards if not card.joker], return_counts=True
        )
        frequencies = list(sorted(frequencies, reverse=True))
        jokers = sum(1 for card in self.cards if card.joker)

        # Compute strength of this hand
        if jokers == 5 or frequencies[0] + jokers == 5:
            strength = 7  # five of a kind
        elif frequencies[0] + jokers == 4:
            strength = 6  # four of a kind
        elif frequencies[0] + frequencies[1] + jokers == 5:
            strength = 5  # full house
        elif frequencies[0] + jokers == 3:
            strength = 4  # three of a kind
        elif frequencies[0] + frequencies[1] + jokers == 4:
            strength = 3  # two pair
        elif frequencies[0] + jokers == 2:
            strength = 2  # one pair
        else:
            strength = 1  # high card

        self.strength = (strength,) + tuple(card.rank for card in self.cards)

    def __lt__(self, other) -> bool:
        return self.strength < other.strength

    def __str__(self) -> str:
        return "".join(card.kind for card in self.cards)


def compute_total_winnings(hands):
    winnings = 0
    for i, hand in enumerate(sorted(hands)):
        winnings += (i + 1) * hand.bet
    return winnings


if __name__ == "__main__":
    hands = []
    for row in read_input("Day07-Puzzle"):
        parts = row.split(" ")
        hands.append(Hand(parts[0], int(parts[1])))

    print(f"Solution 1: {compute_total_winnings(hands)}")

    # Activate jokers
    hands = [Hand(str(hand), hand.bet, joker=True) for hand in hands]
    print(f"Solution 2: {compute_total_winnings(hands)}")
