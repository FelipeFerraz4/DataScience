jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome:'))
jogos = int(input('Quantas partidas jogadas: '))
for i in range(0, jogos):
    partidas.append(int(input(f'Quantos gols na {i+1}° partidas: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(jogador['gols'])


print(jogador)
for i, j in jogador.items():
    print(f'O {i} tem valor {j}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i , j in enumerate(jogador['gols']):
    print(f'Na partida {i} foi {j} gols')
print(f'O total de gols é {jogador["total"]}')

# data = {'nome': str(input('Digite o seu nome: ')),
#         'jogos': int(input('Digite a quantidade de jogos: ')),
#         'partidas': {}}
# for i in range(0, data['jogos']):
#     data['partidas'][i] = int(input(f'Digite a quantidade de gols no {i+1}° partida: '))
#
#
# soma = 0
# for i in range(0, data['jogos']):
#     soma += data['partidas'][i]
# data['soma'] = soma
#
# print('O jogador {} jogou {} partidas'.format(data['nome'], data['jogos']))
# for i, j in data['partidas'].items():
#     print('Na partida {} ele fez {} gols'.format(i+1, j))
# print('END')
