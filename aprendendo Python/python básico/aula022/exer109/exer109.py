from aula022.exer109 import moeda

# Main program
valor = int(input('Digite um valor: '))
print(f'Um aumento de {20}% em {moeda.real(valor)} é {moeda.aumentar(valor, 20, True)}')
print(f'Uma redução de {10}% em {moeda.real(valor)} é {moeda.diminuir(valor, 10, True)}')
print(f'O dobro de {moeda.real(valor)} é {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.real(valor)} é {moeda.metada(valor, True)}')
