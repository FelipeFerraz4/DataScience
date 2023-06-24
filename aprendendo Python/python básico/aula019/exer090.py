data = {}
data['nome'] = str(input('Type your name: '))
data['media'] = float(input('Type your average: '))
if data['media'] < 7:
    data['situação'] = 'reprovado'
else:
    data['situação'] = 'aprovado'
print('O aluno {} tem media {} e está {}'.format(data['nome'], data['media'], data['situação']))
