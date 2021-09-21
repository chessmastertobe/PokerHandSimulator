# Poker Hand Simulator by Derek "Jex" Sneddon
import deck
import card
from itertools import combinations

def main():
    curDeck = deck.Deck()
    curDeck.buildDeck()
    deckList = generateCombinations(curDeck.getDeckList())
    print("RoyalFlushes:", str(checkForRoyalFlushes(deckList)))
    checkHands(deckList)

# there are 2598960 ways to get 5 cards from deck of 52 cards
def generateCombinations(lst):
    comboList = list(combinations(lst, 5))
    # Deck format
    # [ (card("diamonds", "red", "ace"),card())
    #   ...
    # ]


    print("Total combinations:", str(len(comboList)))



    return comboList

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

def checkForRoyalFlushes(deckList):
    #print(deckList[0][0].getColor())
    total = 0
    '''
    for i in len(deckList):
        if(deckList[i][0].getType() == "ace")
    '''
    # Try a for loop system where we check if an ace is in any of all the cards in the touples of five
    for i in range(len(deckList)):
        # First we look through each of the card combinations in the deck
        # then we loop through each of the touples of five that are
        # the combinations themselves
        hasAce = checkForType(deckList[i], "ace")
        hasKing = checkForType(deckList[i], "king")
        hasQueen = checkForType(deckList[i], "queen")
        hasJack = checkForType(deckList[i], "jack")
        hasTen = checkForType(deckList[i], "ten")
        sameSuit = checkAllSameSuit(deckList[i])
        sameColor = checkAllSameColor(deckList[i])

        if(hasAce == True
        and hasKing == True
        and hasQueen == True
        and hasJack == True
        and hasTen == True
        and sameSuit == True
        and sameColor == True):
            total += 1


    return total

def checkForType(cardset, type):
    hasType = False
    for i in range(len(cardset)):
        if(cardset[i].getType() == type):
            hasType = True
            # if we found the type then we can break out of the loop
            break
    return hasType

def checkAllSameSuit(cardset):
    suit = cardset[0].getSuit()
    # if all are going to have the same suit, it will be idential to the first
    counter = 0
    for i in range(len(cardset)):
        if(cardset[i].getSuit() == suit):
            counter += 1
    # if the counter is 5, then they are all in the same suit
    return counter == 5

def checkAllSameColor(cardset):
    color = cardset[0].getColor()
    # if all are going to have the same suit, it will be idential to the first
    counter = 0
    for i in range(len(cardset)):
        if(cardset[i].getColor() == color):
            counter += 1
    # if the counter is 5, then they are all in the same suit
    return counter == 5

def evalutateSeries(cardset):
    return






if __name__ == "__main__":
    main()
