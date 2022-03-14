import pickle
def main():
    file = open('data.dat', 'wb')
    again = 't'
    while again.lower() == 't':
        save_data(file)
        again = input('Enter "t" if you want to save another data.')
    file.close()
def save_data(file):
    data = {}
    data['name'] = input('Enter Your name:')
    data['age'] = input('Enter Your age:')
    data['weight'] = input('Enter  your weight:')
    pickle.dump(data, file)
main()