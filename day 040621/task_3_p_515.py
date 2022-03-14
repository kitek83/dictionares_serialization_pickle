dct = {'Kris': 20, 'Jack':30, 'Dawid':100, 'Jan': 10}
if 'Jan' in dct:
    print(dct['Jan'])
else:
    print('Name was not fount.')
print('-------------------')
if 'Jack' in dct:
    del dct['Jack']
for k, v in dct.items():
    print(k,v)
print('--------------------')
set1 = set([10,20,30,40])
print(set1)
for k in set1:
    print(k)
print('=================')
set2 = set([1,2,3,4,5])
set3 = set([4,5,6,7,8])
set4 = set2 | set3
print(set4)
set5 = set2 & set3
print(set5)
set6 = set2 - set3
print(set6)
print('---------------')
set7 = set3 - set2
print(set7)
set8 = set2 ^ set3
print(set8)











