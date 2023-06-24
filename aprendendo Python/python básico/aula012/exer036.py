priceHouse = float(input('Qual o valor da casa: '))
salary = float(input('Qual o seu salário: '))
yearsToPay = float(input('Quantos anos para pagar: '))
installment = priceHouse / (yearsToPay*12)
print('parcela R${:.2f}'.format(installment))
if installment > (salary * 0.3):
    print('funding denied')
else:
    print('approved funding')
