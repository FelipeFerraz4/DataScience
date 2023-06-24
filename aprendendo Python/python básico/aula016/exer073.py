timeCapeonatoBrasileiro = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
                       'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo',
                       'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino',
                       'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
tamanho = len(timeCapeonatoBrasileiro)
# timeCapeonatoBrasileiro[0:5]
for i in range(0, 5):
    print(f'{i + 1}° colocado: {timeCapeonatoBrasileiro[i]}')
print('')
# timeCapeonatoBrasileiro[-4:]
for i in range(tamanho - 1, tamanho - 5, -1):
    print(f'{i + 1}° colocado: {timeCapeonatoBrasileiro[i]}')
print('')
print(sorted(timeCapeonatoBrasileiro))
print('')
try:
    timeCapeonatoBrasileiro.index('Chapecoense')
except ValueError:
    print('Chapecoense não está na série A')
