#Funções Parte 1
def mostrarlinha():
    print('--------------')


mostrarlinha()
print('SISTEMA DE ALUNOS')
mostrarlinha()
#parâmetro
def mensagem(msg):
    print('--------------')
    print(msg)
    print('--------------')


mensagem('CURSO EM VÍDEO')
mensagem('APRENDA PYTHON')
#prática 1
print('prática 1')
def soma(a, b):
    s = a + b
    print(s)
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=4, a=5)
#prática 2 - empacotamento
print('prática 2')
def contador(*num):
    print(num)
    for valor in num:
        print(f'{valor}', end='')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#prática 3
print('prática 3')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

#prática 4
print('prática 4')
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)