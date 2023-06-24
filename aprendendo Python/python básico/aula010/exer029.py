kilometers = float(input('type the speed of car in kilometers: '))
if kilometers > 80:
    trafficTicket = (kilometers-80) * 7
    print('Driver was fined and the fine is ${:.2f}'.format(trafficTicket))
else:
    print('Driver was not fined')
