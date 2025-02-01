print('{:=^40}'.format('LOJAS GUANABARA'))
v = float(input('Digite o valor total a ser pago: '))
print('''Forma de Pagamento:
[ 1 ] valor à vista no dinheiro
[ 2 ] à vista no cartão
[ 3 ] em 2x no cartão
[ 4 ] em 3x ou mais no cartão''')
s = int(input('Como gostaria de pagar: '))
if s == 1:
    desc = v - (10 * v / 100)
    print('A compra de R${:.2f} tem 10% de desconto no pagamento à vista\nO total a ser pago R${:.2f}'.format(v, desc))
elif s == 2:
    desc = v - (5 * v / 100)
    print('A compra de R${:.2f} tem 5% de desconto no pagamento à vista\nO total a ser pago R${:.2f}'.format(v, desc))
elif s == 3 or 4:
     p = int(input('número de parcelas: '))
     if p == 2:
         vpp = v / p
         print('O valor total a ser pago R${:.2f} em {}X de R${}'.format(v, s, vpp))
     elif p > 3:
         acres = v + (10 * v / 100)
         vpp = acres / p
         print('O valor total a ser pago R${:.2f} em {}X de R${:.2f}'. format(acres, p, vpp))
print('Obrigado pela preferência!')
print('='*35)
