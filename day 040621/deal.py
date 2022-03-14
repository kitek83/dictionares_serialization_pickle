def card():
    cards = {'AS': 1, '1 pik': 1, '2 pik': 2,
             '3 pik': 3, '4pik': 4, '5 pik': 5,
             '6 pik':6, '7 pik':7, '8pik':8,
             '9 pik': 9, '10 pik':10, 'jack': 1,
             'dame':1}
    return cards

def draw_lots(cards, number):
    on_hands = 0
    for count in range(number):
        card, value = cards.popitem()
        print('You got the following cards:',card)
        on_hands += value
    print('Total value of your cards is:', on_hands)