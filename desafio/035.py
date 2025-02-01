a = int(input('Digite o primeiro segmento: '))
b = int(input('Digite o segundo segmento: '))
c = int(input('Digite o terceiro segmento: '))
if (b - c) < a < (b + c):
    print('Os segmentos acima podem formar um triângulo')
else: print('Os segmentos acima não podem formar um triângulo')