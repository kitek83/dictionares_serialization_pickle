#program reads serialized file
import pickle
file = open('mydata.dat', 'rb')
print(pickle.load(file))
file.close()