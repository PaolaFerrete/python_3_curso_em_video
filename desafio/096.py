def area(l,c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m^2')


print('CONTROLE DE TERRENOS')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)