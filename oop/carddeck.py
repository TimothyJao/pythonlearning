from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return self.value + " of " + self.suit

class Deck:
    def __init__(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    
    def __repr__(self):
        return "Deck of " + str(self.count()) + " cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    
    def shuffle(self):
        if self.count() == 52:
            shuffle(self.cards)
            return self
        else:
            raise ValueError("Only full decks can be shuffled")
    
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)
