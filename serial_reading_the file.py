import pickle
file = open('phonebook.dat','rb')
print(pickle.load(file))
text = 'HELLO KRIS'
text1 = text.lower()
print(text1)

data = {}
data['name'] = input('Enter name:')
data['age'] = input('Enter age:')
data['weight'] = input('Enter weight:')
print(data)