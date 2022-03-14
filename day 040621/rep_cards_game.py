import deal
def main():
    deck = deal.card()
    number = int(input('Enter number of cards you want to take:'))
    deal.draw_lots(deck, number)

main()

