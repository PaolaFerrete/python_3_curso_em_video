c = s = n = 0
while n != 999:
    n = int(input('Digite um número: [999 para sair]: '))
    if n == 999:
        print('Você digitou {} números e a soma entre eles foi {}'.format(c, s))
    else:
        s += n
        c += 1
#outra forma
c = s = n = 0
n = int(input('Digite um número: [999 para sair]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número: [999 para sair]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(c, s))
