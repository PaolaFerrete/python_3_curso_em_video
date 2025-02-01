lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Nn':
        break
print('*=*' * 30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')



