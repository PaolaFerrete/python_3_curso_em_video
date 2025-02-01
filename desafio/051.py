t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
pa = 0
print('{}'.format(t), end=' -> ')
for c in range(1, 10):
    pa = t + r
    print('{}'.format(pa), end=' -> ')
    t = pa
print('ACABOU')

#outra forma

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razao
for c in range(primeiro, décimo, razao):
    print('{}'.format(c), end='-> ')
print('Acabou')