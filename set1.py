myset = set(['jeden', 'dwa', 'trzy'])
print(myset)
print(len(myset))
myset2 = set()
myset2.add(1)
myset2.add(2)
myset2.add(3)
print(myset2)
myset3 = set([1,2,3])
myset3.update([4,5,6])
print(myset3)
print('--------------------')
set4 = set([3,4,5])
set5 = set([6,7,8])
set4.update(set5)
print(set4)
print(set5)