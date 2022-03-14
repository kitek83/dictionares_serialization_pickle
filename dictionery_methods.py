phonebook = {'Kris':'732939996','Jack':'4555887','Joanna':'645458'}
print(phonebook)
print(phonebook.get('Kris','element wasn\'t found'))
print(phonebook.get('Adam','element wasn\'t found'))
print(phonebook.items())
print('----------------------')
phonebook['Gorge'] = '998887878'
print(phonebook)