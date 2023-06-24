salary = float(input('type the your salary: $'))
if salary > 1250:
    newSalary = salary * 1.1
else:
    newSalary = salary * 1.15
print('Your new salary are ${}'.format(newSalary))
