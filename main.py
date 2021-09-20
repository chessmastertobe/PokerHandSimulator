# Poker Hand Simulator by Derek "Jex" Sneddon
import deck
import card
from itertools import combinations

def main():
    curDeck = deck.Deck()
    curDeck.buildDeck()
    deckList = generateCombinations(curDeck.getDeckList())
    checkForRoyalFlush(deckList)

# there are 2598960 ways to get 5 cards from deck of 52 cards
def generateCombinations(lst):
    total = list(combinations(lst, 5))
    # Deck format
    # [ (card("diamonds", "red", "ace"),card())
    #   ...
    # ]


    print("Total combinations:", str(len(total)))

    return total

# recieves a list of touples of five length
def checkHands(lst):
        # Check for Royal Flushes
        # A, K, Q, J, 10, all of the same suit

        # Check for Straight Flushes
        # Five cards in a sequence, all in the same uit

        # Check for Four of a Kind
        # All four cards of the same rank

        # Check for Full House
        # Three of a kind with a pair

        # Check for Flush
        # Any five cards of the same suit, but not in a sequnce

        # Check for Straight
        # Five cards in a squence, but not of the same suit

        # Three of a Kind
        # Three cards of the same rank

        # Two Pair
        # Two different pairs

        # Pair
        # Two cards of the same rank

        # If none of the above occur, then nothing
    return

def checkForRoyalFlush(deckList):
    #print(deckList[0][0].getColor())
    total = 0
    '''
    for i in len(deckList):
        if(deckList[i][0].getType() == "ace")
    '''
    return






if __name__ == "__main__":
    main()
