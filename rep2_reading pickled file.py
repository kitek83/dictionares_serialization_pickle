import pickle
def main():
    in_file = open('info2.dat', 'rb')
    end_of_file = False
    while not end_of_file:
        try:
            data = pickle.load(in_file)
            display(data)
        except EOFError:
            end_of_file = True
    in_file.close()
def display(data):
    print('name:', data['name:'])
    print('age:', data['age:'])
    print('weight:', data['weight:'])



main()