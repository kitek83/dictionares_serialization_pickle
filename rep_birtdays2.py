LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    birthdays = {}
    file = open('birth.txt', 'a')
    file.close()
    choice = 0
    while choice != QUIT:
        choice = get_menu()
        if choice == LOOK_UP:
            look_up(birthdays)
        if choice == ADD:
            add(birthdays)
        if choice == CHANGE:
            change(birthdays)
        if choice == DELETE:
            delete(birthdays)
def get_menu():
    print()
    print('This is the menu for the program.')
    print('Please choose the following option:')
    print('1.Look for the name.')
    print('2.Adding the name.')
    print('3.Changing date of birthday.')
    print('4.Delete the name.')
    print('5.Quit the program.')
    choice = int(input('Enter the correct number from the menu:'))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter correct number from the menu.'))
    return choice
def look_up(birthdays):
    name = input('Enter the first and last name:')
    if name in birthdays:
        print(birthdays[name])
    else:
        print('Searched name was not found.')
def add(birthdays):
    name = input('Enter the name and surname:')
    bdate = input('Enter the birth date')
    if name not in birthdays:
        birthdays[name] = bdate
        file = open('birth.txt', 'a')
        file.write(str(birthdays))
        file.close()
def change(birthdays):
    name = input('Enter the name ans surname:')
    if name in birthdays:
        bdate = input('Enter the correct date of birth:')
        birthdays[name] = bdate
        file = open('birth.txt', 'a')
        file.write(str(birthdays))
    else:
        print('Searched name wasn\'t found.')
def delete(birthdays):
    name = input('Enter the name to be deleted:')
    if name in birthdays:
        del birthdays[name]
        file = open('birth.txt')
        file.write(str(birthdays))
        file.close()
    else:
        print('searched name wasn\'t found.')


main()