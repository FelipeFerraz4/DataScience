from random import randint
from time import sleep
guesses = int(input('Type the number of guesses: '))
numbers = []
print('{} {:^35} {}'.format('\033[0:32m', 'Prize draw', '\033[m'))
print('-'*40)
for i in range(0, guesses):
    sleep(1)
    guess = []
    count = 0
    while True:
        number = randint(1, 60)
        if number not in guess:
            guess.append(number)
            count += 1
        if count == 6:
            break
    guess.sort()
    print(f'Drawn numbers: {guess}')
    numbers.append(guess[:])
print('-'*40)
print('END')