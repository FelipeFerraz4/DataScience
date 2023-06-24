def arqexiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    except Exception as erro:
        print(f'O problema foi {erro.__class__}')
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as erro:
        print(f'Erro, o problema foi {erro.__class__}')
    else:
        print('O arquivo foi criado')


def lerarquivo(arq):
    try:
        a = open(arq, 'rt')
    except Exception as erro:
        print(f'Erro, o problema foi {erro.__class__}')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<35} {dado[1]:<6}')
        print('-' * 43)
    finally:
        a.close()


def cadastrar(arq):
    from aula023.exer115 import auxiliar
    nome = auxiliar.name('Digite o seu nome: ')
    idade = auxiliar.inter('Digite a sua idade: ')
    try:
        a = open(arq, 'at')
    except Exception as erro:
        print('Erro ao abrir o arquivo')
        print(f'O problema foi {erro.__class__}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except Exception as erro:
            print('Erro ao escrever no arquivo')
            print(f'O problema foi {erro.__class__}')
        else:
            print('Cadastrado com sucesso!')
            a.close()
