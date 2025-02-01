print('Gerador de PA')
print('-==-'*5)
t = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
c = 1
while c <= 10:
    print('{}'.format(t), end='->')
    t = t + r
    c += 1
print(' Acabou')
print('-==-'*5)