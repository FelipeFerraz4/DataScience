firstTermAP = float(input('type the first term of AP: '))
commonDifference = float(input('type the common difference of AP: '))
cont = 0
while cont < 10:
    print('{}° term: {}'.format((cont+1), firstTermAP + (commonDifference*cont)))
    cont += 1
