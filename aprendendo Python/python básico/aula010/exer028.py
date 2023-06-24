import random
number = random.randint(0, 5)
numberUser = int(input('try to guess the number between 0 and 5: '))
if number == numberUser:
    print('User win, number was {}'.format(number))
else:
    print('user lose, number was {}'.format(number))
