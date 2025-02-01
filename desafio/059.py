n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
opc = 0
while opc != 5:
    print('=-=='*10)
    print('[ 1 ] SOMAR\n'
          '[ 2 ] MULTIPLICAR\n'
          '[ 3 ] MAIOR\n'
          '[ 4 ] NOVOS NÚMEROS\n'
          '[ 5 ] SAIR')
    opc = int(input('>>>>>>>> Qual a sua opção?' ))
    if opc == 1:
        s = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, s))
    elif opc == 2:
        m = n1 * n2
        print('O resultado de {} X {} = {}'.format(n1, n2, m))
    elif opc == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
    elif opc == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
        opc = 0
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
print('=-=='*10)