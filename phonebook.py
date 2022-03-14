phonebook = {'Kris':'732939996','Jack':'4555887','Joanna':'645458'}
print(phonebook['Kris'])
print(phonebook)
phonebook['Jan'] = '44456568'
phonebook['Patryk'] = '558894'
print(phonebook)
del phonebook['Patryk']
print(phonebook)
print(len(phonebook))
if 'Jan' in phonebook:
    del phonebook['Jan']
print(phonebook)
print('---------------------')
test_score = {'Jack': [55,66,88],'Kris':[88,99,98],'Patryk':[11,22,12]}
print(test_score['Jack'])
print('---------------------------------------')
phone2 = {}
phone2['Kris'] = '45454994'
phone2['Mark'] = '5563364'
phone2['Daniel'] = '778897'
print(phone2)