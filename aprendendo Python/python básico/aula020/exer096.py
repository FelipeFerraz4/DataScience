def header(phase):
    width = 50
    print('-'*width)
    print(f'{phase:^50}')
    print('-'*width)

def area(width, height):
    print('A área do terreno é {} metros quadrados'.format(width*height))


header('Área do terreno')
largura = float(input('Largura em metros: '))
altura = float(input('Altura em metros: '))
area(largura, altura)
