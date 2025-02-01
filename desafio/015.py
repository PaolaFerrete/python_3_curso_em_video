km = float(input('Digite o total de Km percorrido: '))
d = int(input('Digite o total de dias: '))
Tot = (km * 0.15) + (d * 60)
print('O valor total a ser pago por {}Km em {} dias é de R${:.2f}'.format(km, d, Tot ))