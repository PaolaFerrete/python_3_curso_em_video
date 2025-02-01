n = int(input('Digite um número entre 0 e 5: '))
lista = [0, 1, 2, 3, 4, 5]
import random
escolhido = random.choice(lista)
if escolhido == n:
    print('Você Venceu!')
else:
    print('Você perdeu!')

#outra forma
from random import randint
computador = randint(0,5)
print('Tente adivinhar um número entre 0 e 5')
jogador = int(input('Digite um número: '))
if jogador == computador
    print('Você venceu!')
else:print ('Você perdeu!')
