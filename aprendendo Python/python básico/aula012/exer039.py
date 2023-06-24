from datetime import date
yearOfBirth = int(input('what year were you born: '))
# currentYear = date.today().year
currentYear = date.today()
currentYear = str(currentYear)[0:4]
difference = (int(currentYear)) - yearOfBirth
if difference < 18:
    difference = 18 - difference
    print('Você ainda vai se alistar no serviço militar em {} anos'.format(difference))
elif difference == 18:
    print('Está na hora de se alistar no serviço militar')
else:
    difference = difference - 18
    print('Já passou do tempo do alistamento em {} anos'.format(difference))
