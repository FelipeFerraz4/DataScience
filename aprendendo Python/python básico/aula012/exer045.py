import random
computerChooses = random.choice(['pedra', 'papel', 'tesoura'])
computerChooses = str(computerChooses).upper()
print('{:40}'.format('Jokenpô'))
userChooses = str(input('Escolha um: pedra - papel - tesoura: ')).upper()
print('computador escolhe {}'.format(computerChooses))
if computerChooses == 'TESOURA' and userChooses == 'PEDRA':
    print('\033[32muser win')
elif computerChooses == 'PEDRA' and userChooses == 'PAPEL':
    print('\033[32muser win')
elif computerChooses == 'PAPEL' and userChooses == 'TESOURA':
    print('\033[32muser win')
elif computerChooses == userChooses:
    print('\033[34mthe match draws')
else:
    print('\033[31muser lose')
