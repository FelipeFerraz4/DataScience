number = int(input('type a number: '))
thousands = number//1000
number = number % 1000
hundreds = number//100
number = number % 100
tens = number // 10
ones = number % 10
print('thousands = {}\nhundreds = {}\ntens = {}\nones = {}'.format(thousands, hundreds, tens, ones))
