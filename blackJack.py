import random

blackJackNumber = 21
deck = []
playerHand = []
dealerHand = []

#Creates 52 cards/ Parameter chooses the amount of times the variable (cards) gets duplicated
def generateCard(amount):
    for card in range(amount):
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        deck.extend(cards)

def restartGame():
    deck.clear()
    generateCard(4)
    playerHand.clear()
    dealerHand.clear()

#deals out card to chosen player
def dealCard(person):
    card = random.choice(deck)
    person.append(card)
    deck.remove(card)

#Adds up the points a player got
def findTotal(person):
    sum = 0
    face = ["J","Q","K"]
    for card in person:
        if card in range (1,11):
            sum += card
        elif card in face:
            sum += 10
        else:
            if sum > 11:
                sum += 1
            else:
                sum += 11
    return sum

#makes the dealer hit when the deck is lower than 16
def dealDealerCard():
    if findTotal(dealerHand) < 15:
        dealCard(dealerHand)

#deals everyone cards
def dealAll():
    for i in range (2):
        dealCard(dealerHand)
        dealCard(playerHand)
    dealDealerCard()





