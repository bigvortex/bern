import cards
import players

CARDS_PER_HAND = 5
        
class Game:
    def __init__(self):
        self.current_Player = None
        self.deck = cards.Deck()
        self.game_players= []

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

        #First player added becomes current player
        if not self.game_players:
           self.current_Player = new_player

        self.game_players.append(new_player)

