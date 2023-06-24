peso = float(input('digite o seu peso em kilo: '))
altura = float(input('Digite a sua altura em metro: '))
imc = peso / (altura * altura)
print('IMC = {}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('peso ideal')
elif imc < 30:
    print('sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
