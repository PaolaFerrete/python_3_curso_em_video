v = float(input('Digite a sua velocidade: '))
if v > 80:
    m = (v - 80) * 7
    print('MULTADO! Você excedeu o limite permitido de 80 km/h.\nVocê deverá pagar uma multa de R${:.2f}'.format(m))
else: print('Você está dentro do limite permitido!')