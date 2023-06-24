firstNumber = float(input('type the first term of an AP: '))
commonDifference = float(input('type the common difference of an AP: '))
for i in range(0, 10, 1):
    print('{:2}° term = {}'.format(i+1, firstNumber + (i*commonDifference)))
