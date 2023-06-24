from random import randint
win = True
counter = 0
while win:
    userChoice = 'xxx'
    numberComputer = randint(1, 2)
    while userChoice != 'EVEN' and userChoice != 'ODD':
        userChoice = str(input('Choice between even and odd: ')).strip().upper()
    numberUser = int(input('Type a number: '))
    if userChoice == 'EVEN':
        if (numberUser + numberComputer) % 2 == 0:
            print('Computer choice {}'.format(numberComputer))
            print(f'\033[0:32mYou win\033[m')
            counter += 1
        else:
            print('Computer choice {}'.format(numberComputer))
            print('{}You lose{}'.format('\033[0:31m', '\033[m'))
            win = False
            break
    else:
        if (numberUser + numberComputer) % 2 == 0:
            print('Computer choice {}'.format(numberComputer))
            print('{}You lose{}'.format('\033[0:31m', '\033[m'))
            win = False
            break
        else:
            print('Computer choice {}'.format(numberComputer))
            print('{}You win{}'.format('\033[0:32m', '\033[m'))
            counter += 1
print(f'You won {counter} times')
