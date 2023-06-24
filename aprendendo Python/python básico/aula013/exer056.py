sumAge = 0
biggestAgeMan = 0
nameOlderMan = 'xxx'
womanAgeUnder20 = 0
people = 4
for i in range(0, people, 1):
    name = str(input('type your name: ')).strip()
    age = int(input('type your age: '))
    gender = str(input('type your gender, man or woman: ')).strip().upper()
    sumAge += age
    if gender == 'MAN' and age > biggestAgeMan:
        biggestAgeMan = age
        nameOlderMan = name
    if gender == 'WOMAN' and age < 20:
        womanAgeUnder20 += 1
print('the average age is {}'.format(sumAge/people))
if nameOlderMan == 'xxx':
    print('Not man')
else:
    print('Older man\'s name: {}'.format(nameOlderMan))
if womanAgeUnder20 == 0:
    print('Not woman')
else:
    print('Number of woman under of 20 year: {}'.format(womanAgeUnder20))
