baseball = set(['Justyna', 'Celina', 'Ada','Alicja'])
basketball = set(['Ewa', 'Celina', 'Alicja','Sara'])
print('Here are the players from the team baseball:')
for name in baseball:
    print(name)
print()
print('Here are the players from the team basketball')
for name in basketball:
    print(name)
print()
print('Here are the players playing for one of the teams.')
for name in baseball.union(basketball):
    print(name)