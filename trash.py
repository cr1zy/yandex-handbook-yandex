from itertools import product

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['буби', 'пики', 'трефы', 'черви']
suits.remove(input())
cards.remove(input())
suits_new = ['бубен', 'пик', 'треф', 'червей']

for card, suit in product(cards, suits):
    print(card, suit)

# 10 mins