confirmation = ''
school = []
while True:
    students = []

    name = str(input('Type your name: '))
    students.append(name)

    score = []
    for i in range(0, 2):
        score.append(float(input(f'Type your test score {i+1}: ')))
    students.append(score[:])

    school.append(students[:])

    confirmation = str(input('Would you like to continue, Y/N: '))[0]
    if confirmation in 'Nn':
        break
print('{:^35}'.format('Grade report'))
print('-'*40)
print('{:<6}{:^20}{:>6}'.format('ID.', 'Name', 'Average'))
for i, student in enumerate(school):
    average = (student[1][0] + student[1][1])/2
    print(f'{i:<6}{student[0]:^20}{average:>6}')
print('-'*40)
while True:
    id = int(input('Gostaria de ver as notas de qual aluno, interronper 999: '))
    if id == 999:
        break
    print(f'the student {school[id][0]} have score {school[id][1][0]} and {school[id][1][1]}')
print('END')
