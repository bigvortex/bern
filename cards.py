import random


class Card(object):
    def __init__(self, suit, val, isWild=False):
        self.suit = suit
        self.value = val
        self.IsWild = isWild
   
    def show(self):
        print ("{} of {}".format(self.value, self.suit))

class JokerCard(Card):
    def __init__(self):
       Card.__init__(self,"None", 0,True)
        

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

    def draw_card(self):
        return self.cards.pop()

    def deal_cards(self,cards_per_hand):
        hand = []
        for i in range(1,cards_per_hand+1):
            hand.append(self.draw_card())

        return hand

class Hand:
   def __init__(self):
        cards
  

