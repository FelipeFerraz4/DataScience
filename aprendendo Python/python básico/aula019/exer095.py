time = []
jogador = dict()
partidas = list()
while True:
    jogador['nome'] = str(input('Nome:'))
    jogos = int(input('Quantas partidas jogadas: '))
    partidas.clear()
    for i in range(0, jogos):
        partidas.append(int(input(f'Quantos gols na {i+1}° partidas: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    while True:
        confirmation = str(input('Would you like to continue, Y/N:')).upper()[0]
        if confirmation in 'YN':
            break
        print('Invalid,', end='')
    if confirmation in 'N':
        break
print('id ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('buscar jogador de id, para no 999: '))
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print(f'invalido, não existe jogador com esse id {busca}:')
    else:
        print(f'jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
print('END')

# data = {}
# count = 0
# while True:
#     jogador = {'nome': str(input('Digite o seu nome: ')),
#                'partidas': int(input('Digite a quantidade de jogos: '))}
#     gols = {}
#     for i in range(0, jogador['partidas']):
#         gols[i] = int(input(f'Digite a quantidade de gols no {i+1}° partida: '))
#
#     jogador['gols'] = gols.copy()
#     data[count] = jogador.copy()
#     count += 1
#     confirmation = str(input('Would you like to continue: Y/N: ')).strip()[0]
#     if confirmation in 'Nn':
#         break
# print('_'*70)
# print('{:<4}{:<15}{}{:>40}'.format('ID', 'Nome', 'gols', 'Total de gols'))
# print()
# for i, jogador in data.items():
#     soma = 0
#     for j in range(0, jogador['partidas']):
#         soma += jogador['gols'][j]
#
#     print('{:<4}{:<15}{}{:>20}'.format(i, jogador["nome"], jogador["gols"], soma))
# while True:
#     iden = int(input('Digite o id do jogador: '))
#     if iden == 999:
#         break
#     if iden > count-1 or iden < 0:
#         continue
#     print('O jogador {} jogou {} partidas'.format(data[iden]['nome'], data[iden]['partidas']))
#     for i in range(0, data[iden]['partidas']):
#         print('Na partida {}° ele fez {} gols'.format(i+1, data[iden]['gols'][i]))
# print('END')
