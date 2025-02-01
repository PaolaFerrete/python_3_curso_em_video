nome = str(input('Qual é o seu nome? ')).upper()
if nome == 'PAOLA':
    print('Que nome lindo você tem!')
elif nome == 'DANIEL':
    print('Que nome feio você tem!')
else:
    print('Que nome normal!')
print('Boa Noite')

#calculo da mádia

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
#condição simplificada
print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS!')