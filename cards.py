import random

class Card(object):
    def __init__(self, suit, val, isWild=False):
        self.suit = suit
        self.value = val
        self.IsWild = isWild
        self.card_name = self.get_card_name_from_value(self.value)
    def __repr__(self):
        return ("{} of {}".format(self.card_name, self.suit))
    
    def get_card_color(self):    
        if self.suit=="Clubs" or self.suit=="Spades":
            return "Black" 
        else:
            return "Red"

    def get_card_name_from_value(self,card_value):
        if card_value>1 and card_value<11: 
            return card_value
        elif card_value==1:
            return "Ace"
        elif card_value=="11":
            return "Jack"
        elif card_value=="12":
            return "Queeen"
        elif card_value=="13":
            return "King"
        elif card_value==14:
            return "Ace"

    def is_left_bern():
        pass #implement logic 

    def is_right_bern():
        pass #implement logic 

class Deck(object):
    def __init__(self):
         self.cards = []
         self.build()

    def build(self):
         for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
             for v in range(9,16):
                self.cards.append(Card(s, v))

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


  

