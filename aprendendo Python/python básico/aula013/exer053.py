frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
c = 0
tamanho = len(frase)
print(frase[::-1])

for i in range(0, tamanho, 1):
    if frase[i] == frase[(tamanho-1)-i]:
        c += 1
if tamanho == c:
    print('{}A frase é um palindromo{}'.format('\033[0:32m', '\033[m'))
else:
    print('{}A frase não é um palindromo{}'.format('\033[0:31m', '\033[m'))
