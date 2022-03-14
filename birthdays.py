LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
def main():
    birthdays = {}
    choice = 0
    while choice != QUIT:
        choice = get_menu()
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add_name(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)

def get_menu():
    print('This program is showing the birthdays dates.')
    print('Choose the following nr.')
    print('1.Search fore the birth date.')
    print('2.Add names and birthdays.')
    print('3.Change the date of the birthdays.')
    print('4.Delete entry with birthdays')
    print('5.Quit from the program.')

    choice = int(input('Enter the number from the menu:'))
    while choice < LOOK_UP or choice > QUIT:
        print('You chosed the wrong number.')
        choice = int(input('Enter correct nr of the menu:'))
    return choice

def look_up(birthdays):
    name = input('Enter searched name:')
    print(birthdays.get(name, 'Name wasn\'t fount'))
def add_name(birth):
    name = input('Enter the name:')
    bdate = input('Enter date of birth')
    if name not in birth:
        birth[name] = bdate
    else:
        print('The same name exists in system.')
def change(birthdays):
    name = input('Enter name:')
    if name in birthdays:
        bdate = input('Enter new date of birth:')
        birthdays[name] = bdate
    else:
        print('Searched name wasn\'t fount')
def delete(birthdays):
    name = input('Enter name:')
    if name in birthdays:
        del birthdays[name]
    else:
        print('Searched name wasn\'t found')




main()




















