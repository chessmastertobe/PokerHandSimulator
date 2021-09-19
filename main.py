# Poker Hand Simulator by Derek "Jex" Sneddon
import deck
import card
from itertools import combinations

def main():
    curDeck = deck.Deck()
    curDeck.buildDeck()
    generateCombinations(curDeck.getDeckList())

def assignDeck():
    return

# there are 2598960 ways to get 5 cards from deck of 52 cards
def generateCombinations(lst):
    total = list(combinations(lst, 5))
    # Deck format
    # [ (card("diamonds", "red", "ace"),card())
    #
    # ]
    print("Total combinations:", str(len(total)))

    return





if __name__ == "__main__":
    main()
