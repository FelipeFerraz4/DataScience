firstTermAP = float(input('type the first term of AP: '))
commonDifference = float(input('type the common difference of AP: '))
cont = 0
while cont < 10:
    print('{}° term: {}'.format((cont+1), firstTermAP + (commonDifference*cont)))
    cont += 1
term = 1
while term != 0:
    term = float(input('Quantos termos quer adicionar: '))
    termsCounted = cont
    while cont < (term+termsCounted):
        print('{}° term: {}'.format((cont + 1), firstTermAP + (commonDifference * cont)))
        cont += 1
print('END')
