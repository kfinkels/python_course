from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return f'{self.value} {self.suit}'

        
class Deck:
    def __init__(self):
        suits = ['Hearts','Diamonds','Clubs','Spades'] 
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
        shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError('All cards have been dealt')
        return self.cards.pop()


if __name__ == "__main__":
    deck = Deck()
    cards = set()
    for i in range(52):
        cards.add(deck.deal())
    print(len(cards))

