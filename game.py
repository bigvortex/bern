import cards
import players

class Game(object):
    deck = cards.Deck()
    
    def __init__(self):
        cards_per_hand = 5
        current_Player = None
        deck = cards.Deck()
        game_players= []

    def start_game(self):
        #check number of players
        player_count = len(game_players)
        if player_count==4: 
            deck.shuffle()
        
            for player in game_players:
                player.hand = deck.deal_cards(cards_per_hand)
        else:
            print("You need four players for this game. You have {}".format(player_count))
        
    def add_player(self,player):
        game_players.append(player)


