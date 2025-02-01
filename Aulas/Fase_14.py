for c in range(1, 10):
    print(c, end='')
print('fim')

c = 1
while c < 10:
    print(c, end='')
    c += 1
print('fim')
#1
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('fim')
#2
n = 'S'
while n == 'S':
    r = int(input('Digite um valor: '))
    n = str(input('Quer continuar? [S/N] ')).upper()
print('fim')
#3
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))
#4
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))