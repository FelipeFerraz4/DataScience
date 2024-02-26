valores = input().split()
linhas = int(valores[0])
colunas = int(valores[1])
matriz = []
for x in range(linhas):
    number = input().split()
    linha = []
    for x in number:
        linha.append(int(x))
    matriz.append(linha)
print(matriz)
    