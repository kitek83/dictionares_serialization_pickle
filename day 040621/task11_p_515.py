#program makes serialization of the dictionary
import pickle
cdt = {'Kris':34, 'Jack':25, 'Adam':56}
for ite in cdt:
    print(ite)
for key, val in cdt.items():
    print(key, val)
file = open('mydata.dat', 'wb')
pickle.dump(cdt, file)
file.close()
