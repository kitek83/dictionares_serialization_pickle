def main():
    cards1 = get_cards()
    n_card = int(input('Enter number of cards you want to  take:'))
    deal_card(cards1, n_card)

def get_cards():
    cards = {'As pik':1, '2 pik':2, '3 pik':3,
             '4 pik':4, '5 pik':5,  '6 pik':6,
             '7 pik':7, '8 pik':8, '9 pik': 9,
             '10 pik': 10, 'wale pik':10,
             'dama pik':10, 'krol pik':10}
    return cards
def deal_card(cards1, number_cards):
    if number_cards >= len(cards1):
        number_cards = len(cards1)
    hand_val = 0
    for count in range(number_cards):
        card, value = cards1.popitem()
        print(card)
        hand_val += value
    print('Value of your cards is:', hand_val)
main()