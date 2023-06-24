scoreOfExam1 = float(input('Score of exam 1: '))
scoreOfExam2 = float(input('Score of exam 2: '))
average = (scoreOfExam1 + scoreOfExam2)/2
if average < 5:
    print('reprovado')
elif average >= 7:
    print('aprovado')
else:
    print('recuperação')
