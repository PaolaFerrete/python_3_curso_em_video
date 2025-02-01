tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')))
print('Você digitou os valores {}'.format(tupla))
print('O número 9 apareceu {} vezes'.format(tupla.count(9)))
if 3 in tupla:
    print('O número 3 apareceu na {}ª posição'.format(tupla.index(3) + 1))
else:
    print('O número 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ',end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
