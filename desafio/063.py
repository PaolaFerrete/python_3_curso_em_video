print('-==-'*10)
print('SEQUÊNCIA DE FIBONACCI')
print('-==-'*10)
s = int(input('quantos termos você quer mostras? '))
t1 = 0
t2 = 1
c = 3
print('{} -> {}'.format(t1, t2), end='')
while c <= s:
    r = t1 + t2
    print(' -> {}'.format(r),end='')
    t1 = t2
    t2 = r
    c += 1
print('-> FIM')