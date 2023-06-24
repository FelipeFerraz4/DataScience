num1 = int(input('Type a number: '))
num2 = int(input('Type a number: '))
num3 = int(input('Type a number: '))
num4 = int(input('Type a number: '))
number = (num1, num2, num3, num4)
print(f'O 9 apareceu {number.count(9)} vezes')
try:
    index3 = number.index(3)
    print(f'Posição do primeiro 3: {index3 + 1}°')
except ValueError:
    print('Não encontrado o número 3')
print('Os pares digitado:', end='')
for i in number:
    if i % 2 == 0:
        print(f' {i} ', end='')
