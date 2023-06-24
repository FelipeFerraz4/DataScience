confirmation = ''
data = []
people = []
count = 0
while True:
    data.append(str(input('type your name: ')).strip().upper())
    data.append(float(input('type your weight: ')))
    people.append(data[:])
    count += 1
    data.clear()
    confirmation = str(input('Would you like to continue, Y/N: '))
    if confirmation in 'Nn':
        break
biggest = smaller = 0
for i in range(0, len(people)):
    if i == 0:
        biggest = people[i][1]
        smaller = people[i][1]
    if biggest < people[i][1]:
        biggest = people[i][1]
    if smaller > people[i][1]:
        smaller = people[i][1]
print('-'*40)
print(f'foram cadastrada {count} pessoas')
print(f'O maior peso {biggest} foi de', end='')
for p in people:
    if p[1] == biggest:
        print(f' {p[0]} ', end='')
print(f'\nO menor peso {smaller} foi de', end='')
for p in people:
    if p[1] == smaller:
        print(f' {p[0]} ', end='')
print('\nEND')
