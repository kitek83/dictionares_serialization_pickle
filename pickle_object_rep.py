import pickle
def main():
    file = open('info.dat','wb')
    again = 't'
    while again.lower() == 't':
        save_data(file)
        again = input('Enter "t" if you want to add data.')
    file.close()
def save_data(file):
    data = {}
    data['name'] = input('Enter the name:')
    data['age'] = input('Enter the age:')
    data['weight'] = input('Enter the weight:')
    pickle.dump(data, file)
    


main()