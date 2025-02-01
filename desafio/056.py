m = 0
maioridade = 0
menor = 0
nome = ''
for p in range(1, 5):
    print('---- {}ª ----'.format(p))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper()
    m += i
    if s == 'M' and i > maioridade:
        maioridade = i
        nome = n
    elif s == 'F' and i < 20:
        menor = menor + 1
print('A média de idade do grupo é de {:.2f}'.format(m / 4))
print('O homem mais velho tem {} e se chama {}'.format(maioridade, nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(menor))
