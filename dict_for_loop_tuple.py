phonebook = {'Kris':'732939996','Jack':'4555887','Joanna':'645458'}
print(phonebook.values())
print()
for val in phonebook.values():
    print(val)
print()
for key, value in phonebook.items():
    print(key, value)
print('---------------------')
print(phonebook.keys())
for x in phonebook:
    print(x)
print('=======================')
for key in phonebook.keys():
    print(key)
print('######################')
key, value = phonebook.popitem()
print(key,value)
print(phonebook)