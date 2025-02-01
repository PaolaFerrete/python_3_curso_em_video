num = [2,5,9,1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.insert(2, 0)
print(num)
num.pop()
print(num)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')
for c, V in enumerate(valores):
    print(f'Na posição {c} encontrei o valore {v}!')
print('Cheguei ao final da lista')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valore: ')))

a = [2, 3, 4, 7]
b = a
c = a[:]
b[2] = 8
print(a)
print(b)
print(c)

