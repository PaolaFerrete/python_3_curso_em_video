v = float(input('Qual a distância da sua viagem? '))
if v <= 200:
    c = v * 0.5
else: c = v * 0.45
print('Você está prestes a começar uma viagem de {}km\nE o preço da passagem será de R${:.2f}'.format(v,c))
