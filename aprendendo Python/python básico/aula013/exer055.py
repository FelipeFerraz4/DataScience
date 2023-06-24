biggest = 0
smaller = 1000
for i in range(0, 5, 1):
    weight = float(input('Type the your weight: '))
    if weight < 0 or weight > 1000:
        print('peso inválido')
    else:
        if weight >= biggest:
            biggest = weight
        if weight <= smaller:
            smaller = weight
print('Biggest weight = {}\nSmaller weight = {}'.format(biggest, smaller))
