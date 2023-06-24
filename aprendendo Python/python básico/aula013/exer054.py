from datetime import date
year = date.today().year
c = 0
for i in range(0, 7, 1):
    yearBirth = int(input('type the your year of birth: '))
    if (year - yearBirth) < 21:
        c += 1
print('{} não atingiram a maioridade'.format(c))
