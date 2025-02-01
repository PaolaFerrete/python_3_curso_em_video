from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for r in tupla:
    print(' {} '.format(r), end='')
print('\nO maior valor sorteado foi: {}'.format(max(tupla)))
print('O menor valor sorteado foi: {}'.format(min(tupla)))
