expression = str(input('Type a expression: ')).strip()
# parentesE = expression.count('(')
# parentesD = expression.count(')')
# if parentesE == parentesD:
#     print(f'The expression -> {expression} <- is valid')
# else:
#     print(f'The expression {expression} isn\'t valid')
pilha = []
for simb in expression:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break # importante retirar esses casos -> )a+b(
if len(pilha) == 0:
    print('valid')
else:
    print('invalid')
