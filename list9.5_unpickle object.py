import pickle
def main():
    file = open('data.dat', 'rb')
    end_of_file = False
    while not end_of_file:
        try:
            bf = pickle.load(file)
            display_file(bf)
        except EOFError:
            end_of_file = True
    file.close()

def display_file(data):
    print('Name:',data['name'])
    print('Age:',data['age'])
    print('Weight:',data['weight'])
    print()

main()