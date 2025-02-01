#break
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
#fstring
print('A soma vale {}'.format(s)) #python 3.0
print(f'A soma vale {s}') #python 3.6
print('A soma vale %s'%(s)) #python 2.0