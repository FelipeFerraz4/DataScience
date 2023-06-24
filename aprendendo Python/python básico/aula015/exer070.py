productSmaller = 0
cheapestProduct = 'x'
confirmation = 'x'
price = -1
counter = 0
productOver1000 = 0
total = 0
while confirmation != 'N':
    nameProduct = str(input('Type product name: ')).strip().upper()
    while price < 0:
        price = float(input('Type product price: '))
    total += price
    if price > 1000:
        productOver1000 += 1
    if counter == 0:
        productSmaller = price
        cheapestProduct = nameProduct
    if price < productSmaller:
        productSmaller = price
        cheapestProduct = nameProduct
    price = -1
    confirmation = 'x'
    counter += 1
    while confirmation not in 'SN':
        confirmation = str(input('Gostaria de continuar, S/N: ')).strip().upper()[0]
print('END')
print(f'${total:.2f} foi o total gasto.')
print(f'{productOver1000} produtos acima de 1000')
print(f'O produto mais barato é {cheapestProduct}')
