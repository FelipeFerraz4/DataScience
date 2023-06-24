from datetime import date
currentYear = date.today()
currentYear = str(currentYear)[0:4]
currentYear = int(currentYear)
# currentYear = date.today().year
yearOfBirth = int(input('what year were you born: '))
difference = currentYear - yearOfBirth
if difference <= 9:
    print('Mirim')
elif difference <= 14:
    print('Infantil')
elif difference <= 19:
    print('Junior')
elif difference <= 20:
    print('Sênior')
else:
    print('Master')
