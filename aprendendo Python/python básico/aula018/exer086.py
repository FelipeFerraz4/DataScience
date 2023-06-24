matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        number = int(input('Type a number: '))
        matriz[i].append(number)
print('-'*20)
for i in range(0, 3):
    print(matriz[i])
print('-'*20)
print('END')
