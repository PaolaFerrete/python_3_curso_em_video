paren = []
teses = []
exp = (str(input('Digite uma expressão: ')))
for i, v in enumerate(exp):
    if v == '(':
        paren.append(v)
    elif v == ')':
        teses.append(v)
if len(paren) == len(teses):
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')

#outra forma
exp = (str(input('Digite uma expressão: ')))
pilha = []
for símb in exp:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) == 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')

