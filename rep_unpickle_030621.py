import pickle
def main():
    end_of_file = False
    file = open('info.dat','rb')
    while not end_of_file:
        try:
            data = pickle.load(file)
            display_d(data)
        except EOFError:
            end_of_file = True
    file.close()
def display_d(data):
    print('Name:',data['name'])
    print('Age:',data['age'])
    print('weigt:',data['weight'])
    print()




main()