matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        number = int(input('Type a number: '))
        matriz[i].append(number)
print('-'*20)

for i in range(0, 3):
    print(matriz[i])

sumEven = 0
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            sumEven += matriz[i][j]
print(f'Even sum = {sumEven}')

sum3 = 0
for i in range(0, 3):
    sum3 += matriz[i][2]
print(f'3° column sum = {sum3}')

biggest2column = 0
for j in range(0, 3):
    if j == 0 or biggest2column < matriz[1][j]:
        biggest2column = matriz[1][j]
print(f'Biggest of 2° column = {biggest2column}')

print('-'*20)
print('END')
