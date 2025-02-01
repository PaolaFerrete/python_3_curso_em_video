dado = list()
pessoas = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if maior < dado[1]:
            maior = dado[1]
        if menor > dado[1]:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('Deseja continuar? [S/N]:  '))
    if resp in 'Nn':
        break
print('-=-' * 30)
print(pessoas)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {maior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi {menor}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]')

