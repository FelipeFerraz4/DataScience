from random import randint
computerNumber = 1
guess = 0
userNumber = 0
while userNumber != computerNumber:
    guess += 1
    computerNumber = randint(0, 10)
    userNumber = int(input('Type a number between 0 and 10: '))
    print('O computador escolheu {}'.format(computerNumber))
print('foi necessário {} palpites para ganhar'.format(guess))
