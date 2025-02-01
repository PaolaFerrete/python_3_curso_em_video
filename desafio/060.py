n = int(input('Digite um número para calcular o Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 1:
    f = f * c
    c -= 1
    print('{} '.format(c), end='')
    print('X ' if c > 1 else '= ', end='')
print('{}'.format(f))


#outra forma
'''from math import factorial
n = int(input('Digite um número para calcular o Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''