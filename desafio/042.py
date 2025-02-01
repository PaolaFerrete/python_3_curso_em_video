t1 = int(input('Primeiro segmento: '))
t2 = int(input('segundo segmento: '))
t3 = int(input('terceiro segmento: '))
if (t2 - t3) < t1 < (t2 + t3):
    print('Os segmentos pode formar um triângulo', end=' ')
    if t1 == t2 and t2 == t3:
        print('Equilátero')
    elif t1 != t2 and t2 != t3:
        print('Escaleno')
    elif t1 == t2 and t1 != t3 or t1 == t3 and t1 != t2 or t2 == t3 and t1 != t2:
        print('Isósceles')
else: print('os segmentos não formam um triângulo')