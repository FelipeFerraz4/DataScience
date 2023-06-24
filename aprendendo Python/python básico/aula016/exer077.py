palavras = ('pao', 'leite', 'cenora', 'batata', 'queijo', 'carne', 'frango', 'ovo')
for palavra in palavras:
    tamanhoPalavra = len(palavra)
    print(f'A palavra {palavra} tem as vogais: ', end='')
    for i in range(0, tamanhoPalavra):
        if palavra[i] in 'aeiouAEIOU':
            print(f'{palavra[i]} ', end='')
    print('')