import pickle
phonebook = {'Kris':'457-5487',
             'Aneta':'7788-889',
             'Jack': '447-889'}
file = open('mydata.dat','wb')
pickle.dump(phonebook,file)
file.close()
file1 = open('mydata.dat','r')
print(file1.read())
file1.close()
print()
in_file = open('mydata.dat', 'rb')
bf = pickle.load(in_file)
print(bf)
