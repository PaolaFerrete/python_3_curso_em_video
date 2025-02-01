#eu que fiz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = soma3coluna = maiorvalor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para {[l], [c]}: '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            soma3coluna += matriz[l][c]
maiorvalor = matriz[1][0]
if maiorvalor < matriz[1][1]:
    maiorvalor = matriz[1][1]
elif maiorvalor < matriz[1][2]:
    maiorvalor = matriz[1][2]
print('-*-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma total de pares é {somap}')
print(f'A soma dos valores da terceira coluna é {soma3coluna}')
print(f'O maior valor da segunda linha é {maiorvalor}')

#Guanabara que fez
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=*=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz [l][c] % 2 = 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz [1][c] > mai:
        mai = matriz[1][c]