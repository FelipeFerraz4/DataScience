def notas(* numbers, situation=False):
    """
    -> sintetiza informações de um turma de alunos sobre suas notas
    :param numbers: as notas dos alunos
    :param situation: falso - não que mostrar a situação da turma e True - mostra a situação
    :return: retonar um dicionário com as informações sintetizada.
    """
    smaller = biggest = count = soma = 0
    for i, num in enumerate(numbers):
        soma += num
        count += 1
        if i == 0:
            biggest = num
            smaller = num
        if biggest < num:
            biggest = num
        if smaller > num:
            smaller = num
    media = soma/count
    classe = {'quantidade de notas': count, 'maior notas': biggest, 'menor nota': smaller, 'media': media}
    if situation:
        if media > 9:
            classe['situation'] = 'Boa'
        elif media > 7:
            classe['situation'] = 'Razoável'
        elif media > 4:
            classe['situation'] = 'Cuidado'
        else:
            classe['situation'] = 'Ruim'
    return classe


# Main program
dic = notas(1, 2, 3, 4, 5, situation=False)
for k, v in dic.items():
    print(f'A {k} é {v}')
help(notas)