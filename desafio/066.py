n = cont = soma = 0
while True:
    print('Digite 999 para sair')
    n = int(input('Digite um número:'))
    if n == 999:
        break
    else:
        soma += n
        cont += 1
print('Você digitou {} números e soma foi {}'.format(cont, soma))