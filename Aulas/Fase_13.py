#1
for c in range (1, 6):
    print('oi')
print('Fim')
#2
for c in range (1, 6):
    print(c)
print('FIM')
#3
for c in range(6, 0, -1):
    print(c)
print('FIM')
#4
n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM')
#5
i = int(input('INÍCIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
#6
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')
#7
s = 0
for c in range (0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))