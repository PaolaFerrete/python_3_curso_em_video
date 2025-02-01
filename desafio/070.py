print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
prodmenor = ' '
preco = tot = menor = totmil = cont = 0
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço R$ '))
    tot += preco
    cont += 1
    if preco >= 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        prodmenor = prod
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R$  {:.2f}'.format(tot))
print('Temos {} produtos custando mais de R$ 1.000,00'.format(totmil))
print('O produto mais barato foi {} que custa R${}'.format(prodmenor, menor))