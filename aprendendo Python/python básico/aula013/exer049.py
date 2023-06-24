number = int(input('type a number: '))
print('{:-^13}'.format(' Tabuada '))
for i in range(0, 11, 1):
    print('{} x {:>2} = {:>4}'.format(number, i, (number*i)))
