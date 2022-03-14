import pickle
SEARCH = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    email = {'Kris': 'kr@wo.pl', 'Jack': 'jl@jk.com', 'Adam': 'as@wg.pl'}
    email['Ada'] = 'ad@sw.pl'
    print(email)
    file = open('emails.dat', 'rb')
    pickle.load(file)
    for k,v in file.items():
       print(k,v)

    choice = 0
    while choice != QUIT:
        choice = menu(email)
        if choice == SEARCH:
            search(email)
        if choice == ADD:
            add(email)
        if choice == CHANGE:
            change(email)
        if choice == DELETE:
            delete(email)

def menu(email):
    print()
    print('Menu:')
    print('1.Search the email by name.')
    print('2.Add  the name and email.')
    print('3.Change the email.')
    print('4.Delete the email')
    print('5.Quit the program.')
    choice = int(input('Enter menu number:'))
    return choice
def search(email):
    name = input('Enter the name:')
    if name in email:
        print(email[name])
    else:
        print('Name wasn\'t found.')
def add(email):
    file = open('emails.dat', 'wb')
    name = input('Enter the name:')
    emai_l = input('Enter the email address:')
    if name not in email:
        email[name] = emai_l
    else:
        print('Entered name already exists.')
    pickle.dump(email, file)
def change(email):
    file = open('emails.dot', 'wb')
    name = input('Enter the name:')
    if name in email:
        e_mail = input('Enter new correct email:')
        email[name] = e_mail
    else:
        print('Name was not found.')
    pickle.dump(email, file)
def delete(email):
    name = input('Enter the name:')
    if name in email:
        del email[name]
    else:
        print('Name was not found.')

























main()

