confirmation = 0
data = {}
count = 0
while True:
    data[count] = {}
    data[count]['name'] = str(input('Type your name: ')).strip()
    data[count]['sex'] = str(input('Type your sex, W/M: ')).strip().upper()[0]
    data[count]['age'] = int(input('Type you age: '))

    count += 1
    confirmation = str(input('Would you like to continue, Y/N: '))
    if confirmation in 'Nn':
        break

soma = 0
woman = []
for i in range(0, count):
    soma += data[i]['age']
    if data[i]['sex'] in 'W':
        woman.append(data[i]['name'])

ageOverAverage = []
ageAverage = soma/count
for i in range(0, count):
    if data[i]['age'] > ageAverage:
        ageOverAverage.append(data[i])

for person in ageOverAverage:
    print(f'A pessoa {person["name"]} do sexo {person["sex"]} de idade',
          f'{person["age"]} tem idade acima da media')

print(woman)
print(f'A media de idade é {ageAverage}')
print(f'{count} pessoas cadastradas')
