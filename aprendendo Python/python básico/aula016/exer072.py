numberExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
          'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
          'dezessete', 'dezoito', 'dezenove', 'vinte')
number = -1
while number > 20 or number < 0:
    number = int(input('Type a number between 0 and 20: '))
print('O número digitado é {}'.format(numberExtenso[number]))
