class Card:

    def __init__(self, suit, color, type):
        self.mSuit = suit
        self.mColor = color
        self.mType = type
        return

    def getSuit(self):
        return self.mSuit

    def getColor(self):
        return self.mColor

    def getType(self):
        return self.mType

    def printCard(self):
        print("Card suit:", self.mSuit, "Card color:", self.mColor, "Card Type:", self.mType)
        return
