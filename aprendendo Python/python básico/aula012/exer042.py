side1 = float(input('digite o primeiro lado do triangulo: '))
side2 = float(input('digite o segundo lado do triangulo: '))
side3 = float(input('digite o terceiro lado do triangulo: '))

if abs(side2 - side3) < side1 < side2 + side3:
    if abs(side1 - side3) < side2 < side1 + side3:
        if abs(side1 - side2) < side3 < side1 + side2:
            print('O triangulo existe')
            triangle = 1
else:
    print('O triangulo não existe')
    triangle = 0

if triangle == 1:
    if side1 == side2 == side3:
        print('tipo: triangulo equilatero')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('tipo: triangulo isósceles')
    else:
        print('tipo: triangulo escaleno')


