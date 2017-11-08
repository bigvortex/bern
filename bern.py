import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print ("{} of {}".format(self.value, self.suit))

class Deck(object):
    def __init__(self):
         self.cards = []
         self.build()

    def build(self):
         for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
             for v in range(9,16):
                self.cards.append(Card(s, v))
                 # print("{} of {}".format(v, s))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand],self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()



card = Card("Clubs", 6)

deck = Deck()
deck.shuffle()
# deck.show()

will = Player("Will")
will.draw(deck).draw(deck).draw(deck).draw(deck).draw(deck)
will.showHand()
# card = deck.draw()
# card.show()

# card.show()


