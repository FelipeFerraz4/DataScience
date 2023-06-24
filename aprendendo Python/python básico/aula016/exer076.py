listProduct = ('pao', 2, 'leite', 4, 'cenora', 4, 'arroz', 3, 'carne', 15, 'linguiça', 14)
tamanhoListProduct = len(listProduct)
print('-'*60, '\nlista de produtos', '-'*20)
for i in range(0, tamanhoListProduct):
    if i % 2 == 0:
        print(f'{listProduct[i]:-<40}', end='')
    else:
        print(f'R$ {listProduct[i]:>5.2f}')

