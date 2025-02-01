pessoas = list()
pessoas = [['Pedro', 25],['Maria', 19], ['João', 32]]
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[1])

# 1 -parte 1
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)
print(teste)
#1 - parte 2
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
print(teste)
# 1 - parte 3
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print(teste)

#2
galera_a = [['joão', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]
for p in galera_a:
    print(p)
    print(p[0])
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos de idade')

#3
galera_b = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('idade: ')))
    galera_b.append(dado[:])
    dado.clear()
print(galera_b)
for p in galera_b:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')