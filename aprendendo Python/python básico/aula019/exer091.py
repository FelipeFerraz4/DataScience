from random import randint
dado = {}
for i in range(0, 4):
    dado[i] = {'jogador': i+1, 'number': randint(1, 6)}
    print('O {}° tirou {}'.format(dado[i]['jogador'], dado[i]['number']))

for i in range(0, 4):
    for j in range(0, 4):
        if dado[i]['number'] > dado[j]['number']:
            troca = dado[i]
            dado[i] = dado[j]
            dado[j] = troca

print('-'*40)
for i in range(0, 4):
    print('O {}° é o jogador {} com {}'.format(i+1, dado[i]['jogador'], dado[i]['number']))
