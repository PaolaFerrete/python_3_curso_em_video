from random import randint
from time import sleep


def sorteando(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(1, 6):
        n = randint(1, 10)
        print(f'{n}', end=' ')
        lst.append(n)
        sleep(0.3)
    print('PRONTO!')


def somando(soma):
    s = 0
    for n in soma:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {soma}, temos {s}')


# programa princpial
numero = list()
sorteando(numero)
somando(numero)
