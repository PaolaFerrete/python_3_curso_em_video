n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    tab = n * c
    print('{} X {:2} = {:2}'.format(n, c, tab))