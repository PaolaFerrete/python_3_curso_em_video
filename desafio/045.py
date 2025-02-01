import random
import emoji
print('Suas opções')
print(emoji.emojize('[ 1 ] Pedra :punch:', use_aliases=True))
print(emoji.emojize('[ 2 ] Papel :hand:', use_aliases=True))
print(emoji.emojize('[ 3 ] Tesoura :v:', use_aliases=True))
n = int(input('Qual sua jogada: '))
print('JO\nKEN\nPO!!!')
print('-=-'*15)
lista = [1, 2, 3]
jok = random.choice(lista)
if n == 1 and jok == 3:
    print(emoji.emojize('Pedra :punch: X :v: Tesoura\nVocê Ganhou!', use_aliases=True))
elif n == 2 and jok == 1:
    print(emoji.emojize('Papel :hand: X :punch: Pedra\nVocê Ganhou!', use_aliase=True))
elif n == 3 and jok == 2:
    print(emoji.emojize('Tesoura :v: X :hand: Papel\nVocê Ganhou!', use_aliases=True))
elif n == 1 and jok == 2:
    print(emoji.emojize('Pedra :punch: X :hand: Papel\nVocê Perdeu!', use_aliases=True))
elif n == 2 and jok == 3:
    print(emoji.emojize('Papel :hand: X :v: Tesoura\nVocê Perdeu!', use_aliases=True))
elif n == 3 and jok == 1:
    print(emoji.emojize('Tesoura :v: X :punch: Pedra\nVocê Perdeu!', use_aliases=True))
elif n == jok:
    print('Empate')