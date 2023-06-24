sex = 'xxx'
age = -1
counterPeopleOver18 = 0
counterMan = 0
counterWomanUnder20 = 0
confirmation = 'x'
while confirmation != 'N':
    while age < 0:
        age = int(input('Type your age: '))
    while sex not in 'WM':
        sex = str(input('Type your sex, W/M: ')).strip().upper()[0]
    if age > 18:
        counterPeopleOver18 += 1
    if sex == 'M':
        counterMan += 1
    if sex == 'W' and age < 20:
        counterWomanUnder20 += 1
    age = -1
    sex = 'xxx'
    confirmation = 'x'
    while confirmation not in 'SN':
        confirmation = str(input('Gostaria de contínuar, S/N: ')).strip().upper()[0]
print(f'{counterPeopleOver18} pessoas tem mais de 18 anos')
print(f'{counterMan} homem foram cadastrado')
print(f'{counterWomanUnder20} mulheres tem menos de 20 anos')
print('END')
