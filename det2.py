set1 =set([1,2,3])
set1.update('abc')
print(set1)
set2 =set([1,2,3,4,5,6,7])
set2.remove(1)
print(set2)
set2.discard(5)
print(set2)
print('------------')
for num in set2:
    print(num)
if 3 in set2:
    print('Value 3 is in the set2')