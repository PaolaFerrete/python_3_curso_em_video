t = c = r = 0
while True:
    print('-'*30)
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if t < 0:
        break
    else:
        for c in range(0, 11):
            r = t * c
            print('{} x {} = {}'.format(t, c, r))
print('Programa Tabuada Encerrado')

