year = int(input('type a year: '))
if (year % 100) != 0 and (year % 4) == 0:
    print('{} is a leap year'.format(year))
elif (year % 400) == 0:
    print('{} is a leap year'.format(year))
else:
    print('{} not is a leap year'.format(year))
from time import sleep
sleep(2)