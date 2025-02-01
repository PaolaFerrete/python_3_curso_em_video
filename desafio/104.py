'''def LeiaInt(b):
    num = str(input(b))
    if num.isnumeric():
        b = int(num)
        return b
    else:
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')



#Programa principal
n = LeiaInt('Digite um número: ')
if type(n) == int:
    print(f'Você acabou de digitar o número {n}')
'''

#Guanabara
def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor


#programa principal
n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

