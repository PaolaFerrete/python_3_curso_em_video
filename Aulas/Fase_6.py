# prática
#soma entre dois números
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

#valores booleanos
n3 = bool(input("Digite um valor: "))
n4 = bool(input("Digite outro valor: "))
print('valores {} e {}'.format(n3, n4,))

# verificação
n = input('digite algo: ')

print('É numérico: ', n.isnumeric())
print('É alfabético: ', n.isalpha())
print('Está em minúsculo: ', n.islower())
print('Está em maiúsculo: ', n.isupper())
