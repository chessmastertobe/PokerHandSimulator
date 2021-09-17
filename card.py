class Card:

    def __init__(self, suit, color, type):
        self.mSuit = suit
        self.mColor = color
        self.mType = type

    def getSuit(self):
        return self.mSuit

    def getColor(self):
        return self.mColor

    def getType(self):
        return self.mType
