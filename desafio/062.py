print('Gerador de PA')
print('-==-'*10)
t = int(input('Digite o primeiro termo: '))
r: int = int(input('Razão: '))
c = 1
tot = 0
m = 10
while m != 0:
    tot += m
    while c <= tot:
        print('{}'.format(t), end='->')
        t = t + r
        c += 1
    print(' PAUSA')
    m = int(input('Quantos termos você quer mostrar? '))
print('-==-'*10)
print('Progressão finalizada com {} termos mostrados'.format(tot))




