distance = float(input('type travel distance in kilometers: '))
if distance > 200:
    cost = distance * 0.45
else:
    cost = distance * 0.5
print('the ticket price is ${}'.format(cost))
