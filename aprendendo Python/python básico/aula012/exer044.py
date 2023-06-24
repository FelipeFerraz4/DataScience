precoNormal = float(input('Digite o preço normal do produto: $'))
condicaoPagamento = float(input('1 - dinheiro/cheque\n'
                                '2 - à vista no cartão\n'
                                '3 - em 2x no cartão\n'
                                '4 - 3x ou mais no cartão\n'
                                'digite a opção de pagamento: '))
if condicaoPagamento == 1:
    print('valor do produto {:.2f}'.format(precoNormal * 0.9))
elif condicaoPagamento == 2:
    print('valor do produto {:.2f}'.format(precoNormal * 0.95))
elif condicaoPagamento == 3:
    print('valor do produto {:.2f}'.format(precoNormal))
elif condicaoPagamento == 4:
    print('valor do produto {:.2f}'.format(precoNormal * 1.2))
else:
    print('\033[31mCondição de pagamento não existente')
