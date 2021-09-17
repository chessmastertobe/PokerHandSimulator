import card

class Deck():


    def __init__(self):
        self.deckList = []

    def buildDeck(self):
        colors = ["red", "black"]
        suits = ["diamonds", "hearts", "spades", "clubs"]
        types = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        countingChecker = 0

        for suit in suits:
            for type in types:
                countingChecker += 1
                if suit == "diamonds" or "hearts":
                    curCard = card.Card("red", suit, type)
                else:
                    curCard = card.Card("black", suit, type)
                self.deckList.append(curCard)
                print(str(countingChecker), "Card:", curCard.getColor(), curCard.getSuit(), curCard.getType())


        print("Deck Length:", str(len(self.deckList)))
