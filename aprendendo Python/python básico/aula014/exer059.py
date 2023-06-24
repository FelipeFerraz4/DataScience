number1 = float(input('Type a number: '))
number2 = float(input('Type a number: '))
operation = 0
while operation != 5:
    print("""Menu de operações: número 1 = {}, número 2 = {}
             [1] Somar
             [2] Multiplicar
             [3] Maior
             [4] Novos números
             [5] Sair do programa""".format(number1, number2))
    operation = int(input('Digite o número da operação escolhida: '))
    if operation == 1:
        print("Sum of numbers = {}".format(number1 + number2))
    elif operation == 2:
        print('Multiplication of numbers: {}'.format(number1 * number2))
    elif operation == 3:
        if number1 > number2:
            print('O maior é o número 1 = {}'.format(number1))
        elif number2 > number1:
            print('O maior é o número 2 = {}'.format(number2))
        else:
            print('the numbers is equals')
    elif operation == 4:
        number1 = float(input('Type a new number: '))
        number2 = float(input('Type a new number: '))
    elif operation == 5:
        print('End')
    else:
        print("invalid operation")
