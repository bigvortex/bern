import cards
import players
import game

def main():
    print("The Program has started")
    #card = Card("Clubs", 6, False)
    this_game =game.Game()

    #Add players to game
    this_game.add_player(players.Player("Will Holcomb"))
    this_game.add_player(players.Player("John Fuex"))
    this_game.add_player(players.Player("Joe Holcomb"))
    this_game.add_player(players.Player("Elvis Presley"))

    this_game.start_game()

    for this_player_index, this_player in enumerate(this_game.game_players): 
        print("Player #{} {}'s hand:\n {}".format(this_player_index + 1,this_player, this_player.showHand("\n")))
        
if __name__ == "__main__":
    main()






