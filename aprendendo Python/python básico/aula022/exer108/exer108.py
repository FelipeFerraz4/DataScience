from aula022.exer108 import moeda
# Main program
valor = int(input('Digite um valor: '))
print(f'Um aumento de {20}% em {moeda.real(valor)} é {moeda.real(moeda.aumentar(valor, 20))}')
print(f'Uma redução de {10}% em {moeda.real(valor)} é {moeda.diminuir(valor, 10)}')
print(f'O dobro de {moeda.real(valor)} é {moeda.dobro(valor)}')
print(f'A metade de {moeda.real(valor)} é {moeda.real(moeda.metada(valor))}')
str(f'R$ {preço}'.replace('.', ','))