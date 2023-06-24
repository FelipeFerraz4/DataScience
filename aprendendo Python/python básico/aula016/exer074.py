import random

# number = (int(random.random()*100), int(random.random()*100), int(random.random()*100),
#           int(random.random()*100), int(random.random()*100))

num1 = int(random.random()*100)
num2 = int(random.random()*100)
num3 = int(random.random()*100)
num4 = int(random.random()*100)
num5 = int(random.random()*100)

biggest = smaller = 0

number = (num1, num2, num3, num4, num5)
tamanhoNumber = len(number)
for i in range(0, tamanhoNumber):
    if i == 0:
        smaller = number[i]
        biggest = number[i]
    # print(max(number))
    if number[i] > biggest:
        biggest = number[i]
    # print(min(number))
    if number[i] < smaller:
        smaller = number[i]
print(number)
print(f'biggest = {biggest}')
print(f'smaller = {smaller}')
