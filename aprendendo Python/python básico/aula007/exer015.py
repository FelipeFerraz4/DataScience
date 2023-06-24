days = int(input('type the amount of days:'))
kilometers = float(input('type the amount of kilometers:'))
cost = (60 * days) + (0.15*kilometers)
print('car cost: ${:.2f}'.format(cost))
