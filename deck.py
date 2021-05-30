import os
import math
import random


def shuffle(x):
    random.shuffle(x)

deck = list()

for i in range(1, 14):
    if i == 1:
        card = "A"
    elif i == 11:
        card = "J"
    elif i == 12:
        card = "Q"
    elif i == 13:
        card = "K"
    else:
        card = str(i)

    deck.append("Spade " + card)
    deck.append("Heart " + card)
    deck.append("Club " + card)
    deck.append("Diamond " + card)

print(deck)

count = 0

while True:
    cmd = input("Enter a command: ")
    if cmd[:4] == "deal":
        shuffle(deck)
        print(deck)
        userCards = ((deck[0] + " " + deck[1]))
        count += 2
        print("User cards: " + userCards)
        dealerCards = deck[0 + count] + " " + deck[1 + count]
        count += 2
    elif cmd[:4] == "draw":
        sharedCards = deck[0 + count]
        count += 5
        print("User cards: " + userCards)
        print("Shared cards: " + sharedCards)
    elif cmd[:4] == "show":
        print("Dealers cards: " + dealerCards)
    elif cmd[:4] == "quit":
        quit()
    else:
        print("Enter a proper command!")
