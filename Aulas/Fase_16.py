#Tuplas
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra Caramba')
for cont in range(0,len(lanche)):
    print(lanche[cont])
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche))

#outro
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))
del(lanche, a, b, c)
