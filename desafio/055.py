a = 0
b = 0
for p in range(1, 6):
    x = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if x > a and a <= b:
        a = x
        b = a
    elif x > a:
        a = x
    elif x < b:
        b = x
print('O maior peso lido foi {}\nE o menor peso foi {}'.format(a, b))
#outraforma
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}\nE o menor peso foi {}'.format(maior, menor))