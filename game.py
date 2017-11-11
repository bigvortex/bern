import cards
import players

CARDS_PER_HAND = 5
        
class Game:
    def __init__(self):
        self.deck = cards.Deck()
        self.game_players= []
        self.trick = Trick()

    def start_game(self):
        #check number of players
        player_count = len(self.game_players)
        if player_count==4: 
            self.deck.shuffle()
        
            for player in self.game_players:
                player.hand = self.deck.deal_cards(CARDS_PER_HAND)
        else:
            print("You need four players for this game. You have {}".format(player_count))
        
    def add_player(self,new_player):

        #First player added becomes current player - todo Move to trick
        if not self.game_players:
           self.trick.current_Player = new_player

        self.game_players.append(new_player)

    def determine_winning_card(card1,card2,card3,card4):
        pass

class Trick: 
    def __init__(self):
        self.bern_suit = None
        self.trump_suit = None
        self.suit_led = None
        self.dealer = None
        self.current_player = none

    def is_left_Bern(this_card):
        if this_card.get_card_color()==