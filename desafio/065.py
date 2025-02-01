n = 'S'
soma = maior = menor = cont = 0
while n == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if num > maior and maior <= menor:
        maior = num
        menor = maior
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    n = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi {}\n'
      'O maior valor foi {} e o menor foi {}'.format(cont, media, maior, menor))

#outra forma maior e menor

if cont == 1:
    maior = menor = num
else:
    if num > maior:
        maior = num
    if num < menor:
        menor = num