n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para converção:')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual {}'.format(n, bin(n)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual {}'.format(n, oct(n)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual {}'.format(n,hex(n)))
else: print('Número inválido')