'''
Some needed var
'''
values = {"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"jack":10,"queen":10,"king":10,"ace":11}
ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace")
suits = ("spades", "hearts", "clubs", "diamonds")

'''
some needed library
'''
import random

'''
Class Cards
'''
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return " :{} of {}".format(self.rank, self.suit)
    def value(self):
        return values[self.rank]
# TEST
# card1 = Card("spades", "king")
# print(card1)
# print(card1.value())

'''
Deck Cards
'''
class Deck():
    def __init__(self):
        self.deckCards = []
        for suit in suits:
            for rank in ranks:
                self.deckCards.append(Card(suit, rank))
    def __str__(self):
        return "cards in deck : {}".format(len(self.deckCards))
    def shuffleDeck(self):
        random.shuffle(self.deckCards)
    def dealOne(self):
        return self.deckCards.pop()
# TEST
# deck1 = Deck()
# print(deck1.deckCards[0].value())
# print(deck1.deckCards[51].value())
'''
Player Class
'''
class Player():
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.playerCards = []
    def addCard(self, newCard):
        self.playerCards.append(newCard)
    def __str__(self):
        return "{} has {} chips left".format(self.name,self.chips)
    def sumScore(self):
        temp = 0
        for card in self.playerCards:
            temp += card.value()
        return temp
    def showCards(self):
        for card in self.playerCards:
            print(card)
    def addChips(self,newChip):
        self.chips += newChip
    def placeBet(self,bet):
        self.chips -= bet
        return bet
    def emptyHand(self):
        self.playerCards = []
    def desc(self):
        print("Player Info")
        print(" :Player's name : {}".format(self.name))
        print(" :{}'s chips : {}".format(self.name,self.chips))

# TEST 
player1 = Player("Jack", 1000)
player1.addCard(Card("spades", "ace"))
player1.addCard(Card("clubs","seven"))
# print(player1.sumScore())
# player1.showCards()
'''
Dealer Class
'''
class Dealer():
    def __init__(self):
        self.dealerCards = []
    def addCard(self, newCard):
        self.dealerCards.append(newCard)
    def sumScore(self):
        temp = 0
        for card in self.dealerCards:
            temp += card.value()
        return temp
    def __str__(self):
        return "dealer has {} cards".format(len(self.dealerCards))
    def showSome(self):
        idx = 1
        print(" :first Card is the mystery card")
        while idx < len(self.dealerCards):
            print(self.dealerCards[idx])
            idx += 1
    def emptyHand(self):
        self.dealerCards = []
# TEST
dealer1 = Dealer()
dealer1.addCard(Card("spades", "queen"))
dealer1.addCard(Card("clubs", "king"))
dealer1.addCard(Card("hearts", "nine"))
# dealer1.showSome()        

# Writing Game Logic

# function to determine the game ended either the player loses or won
# or the dealer busted or the player busted
def checkWin(player, dealer):
    if player.sumScore() > 21:
        return 0
    elif dealer.sumScore() > 21:
        return 1
    elif player.sumScore() <= 21 and player.sumScore() > dealer.sumScore():
        return 2
    elif dealer.sumScore() <= 21 and player.sumScore() < dealer.sumScore():
        return 3
# TEST
# print(checkWin(player1,dealer1))

# The real GAme Logic
def showPlayerDealerCards(player, dealer):
    print("######################")
    print("{}, player Cards".format(player.name))
    player.showCards()
    print("dealer Cards")
    dealer.showSome()
    print("######################")
# TEST
# showPlayerDealerCards(player1, dealer1)

# BET FUNC
def bet():
    while True:
        try:
            betTemp = int(input("Enter your bet: "))
        except:
            print("Invalid Input, please Input again")
        else:
            print("{} chips betted".format(betTemp))
            return betTemp
# MAIN GAME
def main():
    player = Player("Jack", 1000)
    # TEXT UI
    while True:
        if player.chips <= 0:
            print("player {}, You dont have chips, so begone".format(player.name))
            break
        print("#####Simple Blackjack Game#####")
        opt = input("(1) play the game (2) player info (else) Quit the game : ")
        # validating opt player
        if opt == "1":
            # THE REAL GAME LOGIC
            deck = Deck()
            deck.shuffleDeck()
            dealer = Dealer()
            # dealing two cards to both deaker and player
            player.emptyHand()
            dealer.emptyHand()
            # FOR DEALER
            dealer.addCard(deck.dealOne())
            dealer.addCard(deck.dealOne())
            # FOR PLAYER 
            player.addCard(deck.dealOne())
            player.addCard(deck.dealOne())
            
            # BETTING
            betTemp = player.placeBet(bet())
            # PLAYING
            while True:
                # showing cards
                showPlayerDealerCards(player,dealer)
                opt = input("(1) HIT (2) STAND (else) STOP: ")
                if opt == "1":
                    player.addCard(deck.dealOne())
                    dealer.addCard(deck.dealOne())
                elif opt == "2":
                    dealer.addCard(deck.dealOne())
                else:
                    # checking win or not
                    tempCheck = checkWin(player, dealer)
                    if tempCheck == 0:
                        print("You busted Sorry, you loss")
                        break
                    elif tempCheck == 1:
                        print("Dealer busted, you win")
                        player.addChips(betTemp * 2)
                        break
                    elif tempCheck == 2:
                        print("You won CONGRATS")
                        player.addChips(betTemp * 2)
                        break
                    elif tempCheck == 3:
                        print("You loss, SORRY")
                        break
            # pass
        elif opt == "2":
            player.desc()
        # Quitting the game
        else:
            print("Quitting the game")
            player.desc()
            break
    
##### START
if __name__ == "__main__":
    main()
else:
    print("classes has ben imported")