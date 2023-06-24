def voto(yearofbirth):
    from datetime import date
    year = date.today().year
    idade = year - yearofbirth
    if idade < 16:
        return 'Voto negado'
    elif 18 <= idade <= 70:
        return 'Voto obrigatório'
    else:
        return 'Voto opcional'


# Main program
voto = voto(int(input('Digite seu ano de nascimento: ')))
print(voto)
