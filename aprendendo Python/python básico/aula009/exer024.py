town = str(input('What\'s your town: '))
town = town.strip()
town = town.upper()
print('A cidade começa com SANTO: {}'.format('SANTO' in town[0:5]))
