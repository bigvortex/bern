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

    this_game.start()

    #deck = Deck()
    #deck.shuffle()
    # deck.show()


if __name__ == "__main__":
    main()






