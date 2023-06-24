from datetime import date

year = date.today().year

data = {'name': str(input('Type your name: ')),
        'age': year - int(input('type your year of birth: ')),
        'carteira': int(input('Id da carteira de trabalho: '))}

if data['carteira'] != 0:
    data['year of contract'] = int(input('Qual o ano da contratação: '))
    data['salario'] = float(input('Salary: $'))

print('Name: {}'.format(data['name']))
print('Age: {}'.format(data['age']))
print('id carteira: {}'.format(data['carteira']))

if data['carteira'] != 0:
    print('Year of contract: {}'.format(data['year of contract']))
    print('Salary: ${}'.format(data['salario']))
    aposentadoria = (data['year of contract']+35) - (year-data['age'])
    print('Aposentadoria: {}'.format(aposentadoria))
