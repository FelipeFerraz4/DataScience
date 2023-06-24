def leiaint(phase):
    while True:
        try:
            numtext = int(input(phase))
        except (ValueError, TypeError):
            print('Por favor digite um número inteiro valido')
        except KeyboardInterrupt:
            print('\nUsuário preferiu não digitar o valor')
            return 0
        except Exception as erro:
            print(f'O problema foi {erro.__class__}')
        else:
            return numtext


def leiareal(phase):
    while True:
        try:
            num = float(input(phase).replace(',', '.'))
        except (ValueError, TypeError):
            print('Por favor digite um número real valido')
        except KeyboardInterrupt:
            print('\nUsuário preferiu não digitar o valor')
            return 0
        except Exception as erro:
            print(f'O problema foi {erro.__class__}')
        else:
            return num
