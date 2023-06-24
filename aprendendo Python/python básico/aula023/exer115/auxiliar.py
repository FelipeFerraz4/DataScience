def header(phase):
    tamanho = len(phase) + 20
    print('-' * tamanho)
    print(phase.center(tamanho))
    print('-' * tamanho)


def menu(* lista):
    for i, option in enumerate(lista):
        print(f'{i+1} - {option}')
    print('-' * 34)
    while True:
        num = inter('Opção: ')
        if num < 1 or num > 3:
            print('Erro, O valor digitado não está nas opções')
        else:
            return num


def name(phase):
    while True:
        try:
            nome = str(input(phase)).strip()
            if (not nome.isnumeric()) and nome != '':
                return nome
            else:
                print('Erro, não deixe em branco ou deixe só número')
        except KeyboardInterrupt:
            print('\nNome deixado em branco')
        except Exception as erro:
            print(f'O problema foi {erro.__class__}')


def inter(phase):
    while True:
        try:
            num = int(input(phase))
        except (ValueError, TypeError):
            print('Erro, O valor digitado não é um inteiro valido')
        except KeyboardInterrupt:
            print('\nErro, número não informada')
        except Exception as erro:
            print(f'O problema foi {erro.__class__}')
        else:
            return num
