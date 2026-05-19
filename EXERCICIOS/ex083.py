'''
i = str(input('Digite uma expressao matematica'))
a = i.count('(')
f = i.count(')')
if a != f:
    print('expressão invalida')
if a == f:
    print('expressao valida')'''

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta valida')
else:
    print('expressao invalida')
