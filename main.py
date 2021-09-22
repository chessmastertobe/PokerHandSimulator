# Poker Hand Simulator by Derek "Jex" Sneddon
import deck
import card
from itertools import combinations

def main():
    curDeck = deck.Deck()
    curDeck.buildDeck()
    deckList = generateCombinations(curDeck.getDeckList())

    RF = checkForRoyalFlushes(deckList)
    SF = checkForStraightFlushes(deckList)
    FK = checkFourOfAKinds(deckList)
    FH = checkFullHouses(deckList)
    F = checkFlushes(deckList)
    S = checkStraights(deckList)
    TK = checkThreeOfAKinds(deckList)
    TP = checkTwoPairs(deckList)
    P = checkPairs(deckList)

    print("Royal Flushes:", str(RF))
    print("Straight Flushes:", str(SF - RF))
    print("Four of a Kinds:", str(FK))
    print("Full House:", str(FH))
    print("Flushes:", str(F - SF))
    print("Straight:", str(S - SF))
    print("Three of a Kind:", str(TK - FH))
    print("Two Pairs:", str(TP))
    print("Pairs:", str(P - TP - FH))
    print("Nothing:", str(len(deckList) - RF - SF + RF - FK - FH - F + SF - S + SF - TK + FH - TP - P + TP + FH))

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



        # If none of the above occur, then nothing
    return

# Check for Royal Flushes
# A, K, Q, J, 10, all of the same suit
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

# Check for Straight Flushes
# Five cards in a sequence, all in the same suit
def checkForStraightFlushes(deckList):
    '''
    total = 0
    for i in range(len(deckList)):
        if(evalutateSequence(deckList[i]) == True
        and checkAllSameSuit(deckList[i]) == True
        and checkAllSameColor(deckList[i]) == True):
            total += 1
    '''
    total = 0
    possibleSequences = [["ace", "two", "three", "four", "five"],
    ["two", "three", "four", "five", "six"],
    ["three", "four", "five", "six", "seven"],
    ["four", "five", "six", "seven", "eight"],
    ["five", "six", "seven", "eight", "nine"],
    ["six", "seven", "eight", "nine", "ten"],
    ["seven", "eight", "nine", "ten", "jack"],
    ["eight", "nine", "ten", "jack", "queen"],
    ["nine", "ten", "jack", "queen", "king"],
    ["ten", "jack", "queen", "king", "ace"]]

    for i in range(len(deckList)):
        for j in range(len(possibleSequences)):
            if(checkForType(deckList[i], possibleSequences[j][0]) == True
            and checkForType(deckList[i], possibleSequences[j][1]) == True
            and checkForType(deckList[i], possibleSequences[j][2]) == True
            and checkForType(deckList[i], possibleSequences[j][3]) == True
            and checkForType(deckList[i], possibleSequences[j][4]) == True
            and checkAllSameSuit(deckList[i]) == True
            and checkAllSameColor(deckList[i]) == True):
                total += 1
                break
    return total

# Check for Four of a Kind
# All four cards of the same rank
def checkFourOfAKinds(deckList):
    total = 0
    possibleTypes = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
    for i in range(len(deckList)):
        for j in range(len(possibleTypes)):
            if(countCardsOfType(deckList[i], possibleTypes[j]) == 4):
                #Found it!
                total += 1
                break
    return total

# Check for Full House
# Three of a kind with a pair
def checkFullHouses(deckList):
    total = 0
    hasThreeOfAKind = False
    hasPair = False
    possibleTypes = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
    for i in range(len(deckList)):
        # Find 3 of a kind
        for j in range(len(possibleTypes)):
            if(countCardsOfType(deckList[i], possibleTypes[j]) == 3):
                #Found it!
                hasThreeOfAKind = True
                completedType = possibleTypes[j]
                # Check for the pairs, only if a three of kind has been found
                for k in range(len(possibleTypes)):

                    if(countCardsOfType(deckList[i], possibleTypes[k]) == 2
                    and possibleTypes[k] != completedType):
                        #Found it with a pair!
                        hasPair = True
                        total += 1
                        break
                break

    return total

# Check for Flush
# Any five cards of the same suit, but not in a sequnce
# this includes Stright Flushes
def checkFlushes(deckList):
    total = 0
    for i in range(len(deckList)):
        if(checkAllSameSuit(deckList[i]) == True and checkAllSameColor(deckList[i])):
            total += 1

    return total

# Check for Straight
# Five cards in a squence, but not of the same suit
# Includes Straight Flush
def checkStraights(deckList):
    total = 0
    possibleSequences = [["ace", "two", "three", "four", "five"],
    ["two", "three", "four", "five", "six"],
    ["three", "four", "five", "six", "seven"],
    ["four", "five", "six", "seven", "eight"],
    ["five", "six", "seven", "eight", "nine"],
    ["six", "seven", "eight", "nine", "ten"],
    ["seven", "eight", "nine", "ten", "jack"],
    ["eight", "nine", "ten", "jack", "queen"],
    ["nine", "ten", "jack", "queen", "king"],
    ["ten", "jack", "queen", "king", "ace"]]

    for i in range(len(deckList)):
        for j in range(len(possibleSequences)):
            if(checkForType(deckList[i], possibleSequences[j][0]) == True
            and checkForType(deckList[i], possibleSequences[j][1]) == True
            and checkForType(deckList[i], possibleSequences[j][2]) == True
            and checkForType(deckList[i], possibleSequences[j][3]) == True
            and checkForType(deckList[i], possibleSequences[j][4]) == True):
                total += 1
                break
    return total

# Three of a Kind
# Three cards of the same rank
def checkThreeOfAKinds(deckList):
    total = 0
    possibleTypes = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
    for i in range(len(deckList)):
        # Find 3 of a kind
        for j in range(len(possibleTypes)):
            if(countCardsOfType(deckList[i], possibleTypes[j]) == 3):
                #Found it!
                total += 1
                break

    return total

# Two Pair
# Two different pairs
def checkTwoPairs(deckList):
    total = 0
    possibleTypes = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
    for i in range(len(deckList)):
        # Find 2 of a kind
        for j in range(len(possibleTypes)):
            if(countCardsOfType(deckList[i], possibleTypes[j]) == 2):
                #Found it!
                completedType = possibleTypes[j]
                # Check for the pairs, only if a three of kind has been found
                for k in range(len(possibleTypes)):

                    if(countCardsOfType(deckList[i], possibleTypes[k]) == 2
                    and possibleTypes[k] != completedType):
                        #Found it with a pair!
                        total += 1
                        break
                break

    return total

# Pair
# Two cards of the same rank
def checkPairs(deckList):
    total = 0
    possibleTypes = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
    for i in range(len(deckList)):
        # Find 2 of a kind
        for j in range(len(possibleTypes)):
            if(countCardsOfType(deckList[i], possibleTypes[j]) == 2):
                #Found it!
                total += 1
                break

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

def countCardsOfType(cardset, type):
    total = 0
    for i in range(len(cardset)):
        if(cardset[i].getType() == type):
            total += 1
    return total

def evalutateSequence(cardset):
    # checks if we have a set in order
    # Possible sets include:
    # ace, 2, 3, 4, 5
    # ...
    # ten, jack, queen, king, ace

    # Should be fourty different ones
    possibleSequences = [["ace", "two", "three", "four", "five"],
    ["two", "three", "four", "five", "six"],
    ["three", "four", "five", "six", "seven"],
    ["four", "five", "six", "seven", "eight"],
    ["five", "six", "seven", "eight", "nine"],
    ["six", "seven", "eight", "nine", "ten"],
    ["seven", "eight", "nine", "ten", "jack"],
    ["eight", "nine", "ten", "jack", "queen"],
    ["nine", "ten", "jack", "queen", "king"],
    ["ten", "jack", "queen", "king", "ace"]]

    hasAll = False
    for i in range(len(possibleSequences)):
        counter = 0
        for j in range(len(possibleSequences[i])):
            if(checkForType(cardset, possibleSequences[i][j]) == True):
                counter += 1
        if counter == 5:
            #Found it!!
            hasAll = True
            break
    return hasAll






if __name__ == "__main__":
    main()
