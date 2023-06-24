def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} no campeonato')


# Main program
name = str(input('Type your name: '))
g = str(input('Type the number of gols: '))
if g == '':
    if name == '':
        ficha()
    else:
        ficha(name)
else:
    g = int(g)
    if name == '':
        ficha(gols=g)
    else:
        ficha(name, g)
