'''
first class Card
attr : Suit(heart,diamond,spade, club),
rank(2-10,jack,queen,king,ace)
, value(2-14)
'''
### import shuffle
from random import shuffle
# making value dictionary for the cards
values = {"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"jack":11,"queen":12,"king":13,"ace":14}
ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace")
suits = ("spades", "hearts", "clubs", "diamonds")
# fisrt class Card
class Card():
    def __init__(self, suit, rank):
        #String expected
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
    def valueCheck(self):
        return values[self.rank]
'''
Deck card
has shuffle method, and deeal one method
'''
class Deck():
    def __init__(self):
        self.deckOfCards = []
        for suit in suits:
            for rank in ranks:
                self.deckOfCards.append(Card(suit, rank))
    def __str__(self):
        return "Deck has {} cards".format(len(self.deckOfCards))
    def showDeck(self):
        for card in self.deckOfCards:
            print(card)
    def shuffleDeck(self):
        shuffle(self.deckOfCards)
    def dealOne(self):
        return self.deckOfCards.pop()
'''
Player class
has cards attribute, add method, remove method
'''
class Player():
    def __init__(self, name):
        #expect string
        self.name = name
        #empty hand
        self.playerCards = []
    def removeOneCard(self):
        # remove from the top
        return self.playerCards.pop(0)
    def addCards(self,cards):
        if type(cards) == type([]):
            self.playerCards.extend(cards)
        else:
            self.playerCards.append(cards)
    def shuffleCards(self):
        shuffle(self.playerCards)
    def __str__(self):
        return "{} has {} cards left".format(self.name, len(self.playerCards))