import pickle
def main():
    input_file = open('info2.dat', 'wb')
    again = 't'

    while again == 't':
        save_data(input_file)
        again = input('If you want to save more data, press "t"')
    input_file.close()
def save_data(file):
    data = {}
    data['name:'] = input('Enter name:')
    data['age:'] = input('Enter age:')
    data['weight:'] = input('Enter weight:')
    pickle.dump(data, file)

main()