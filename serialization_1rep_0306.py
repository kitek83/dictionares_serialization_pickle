import pickle
#saving file - convert to byte stream
in_file = open('phonebook.dat','wb')
phonebook = {'Kris':'758-7885',
             'Jack': '445-6694',
             'Adam': '1125-667'}
pickle.dump(phonebook, in_file)
in_file.close()


