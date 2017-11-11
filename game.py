import cards
import players

class Game(object):
    def __init__(self):
        cards_per_hand = 5
        current_Player = None
        deck = cards.Deck()
        players= []

    def start_game():
        #check number of players
        player_count = len(players)
        if player_count==4: 
            deck.shuffle()
        
            for player in players:
                player.hand = deck.deal_cards(cards_per_hand)
        else:
            print("You need four players for this game. You have {}".format(player_count))
        
    def add_player(player):
        players.append(player)


