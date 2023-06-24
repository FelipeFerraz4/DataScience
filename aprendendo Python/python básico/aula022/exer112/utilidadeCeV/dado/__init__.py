def leiadinheiro(phase):
    while True:
        valor = str(input(phase)).replace(',', '.').strip()
        if (not valor.isalpha()) and (valor != ''):
            break
        else:
            print(f'Erro, \"{valor}\" não é um preço valido')
    valor = float(valor)
    return valor
