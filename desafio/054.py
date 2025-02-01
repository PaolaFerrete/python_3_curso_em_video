from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    n = int(input('Qual o ano de nascimento {} pessoa: '.format(c)))
    idade = ano - n
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE também {} menores de idade'.format(maior, menor))