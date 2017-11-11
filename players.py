class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return "Player {}".format(self.name)

    def showHand(self):
        hand_display="";
        for this_card in self.hand:
            hand_display = hand_display + str(this_card) + " "
        
        return hand_display
    