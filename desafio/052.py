cores = {'limpa':'\033[m', 'Amarelo': '\033[33m',
         'Branco':'\033[30m', 'Vermelho':'\033[31m',
         'Verde':'\033[32m', 'Azul':'\033[32m',
         'Roxo':'\033[35m', 'Azul Claro':'\033[36m',
         'Cinza':'\033[37m','Preto':'\033[7;30m'}
n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('{}{}{}'.format(cores['Vermelho'], c, cores['limpa']),end=' ')
        cont += 1
    else:
        print('{}{}{}'.format(cores['Amarelo'], c, cores['limpa']), end=' ')
print('\nO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')


