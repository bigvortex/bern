class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return self.name

    def showHand(self, delimiter="\n"):
        hand_display=""
        for this_card in self.hand:
            hand_display = "{}\t{}{}".format(hand_display,this_card, delimiter)
        
        return hand_display
    