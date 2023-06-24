from aula023.exer115 import auxiliar
from aula023.exer115 import arquivo

# Main program
arq = 'Bancodedado.txt'
if not arquivo.arqexiste(arq):
    arquivo.criararquivo(arq)

while True:
    auxiliar.header('Menu principal')
    num = auxiliar.menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema')
    if num == 1:
        auxiliar.header('Ver pessoas cadastradas')
        arquivo.lerarquivo(arq)
    if num == 2:
        auxiliar.header('Cadastrar nova pessoa')
        arquivo.cadastrar(arq)
    if num == 3:
        auxiliar.header('Sair do sistema')
        break
print('END')
