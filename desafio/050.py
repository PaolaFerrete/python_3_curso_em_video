s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você informou {} pares e a soma dos valores foi {}'.format(cont, s))