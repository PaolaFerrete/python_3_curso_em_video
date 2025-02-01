import random
cont = 0
escolhido = random.randint(0, 10)
print('Sou seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10\n'
      'Será que você consegue adivinhar qual foi?')
p = int(input('Qual é o seu palpite? '))
while escolhido != p:
    cont += 1
    if escolhido > p:
        print('Mais... Tente mais uma vez: ')
        p = int(input('Qual é o seu palpite? '))
    elif escolhido < p:
        print('Menos... Tente mais uma vez: ')
        p = int(input('Qual é o seu palpite? '))
print('Parabéns! Você acertou após {} tentativas'.format(cont))

#outra forma
acertou = False
while not acertou:
    p = int(input('Qual seu palpite? '))
    cont += 1
    if p == escolhido:
        acertou = True
    else:
        if p < escolhido:
            print('Mais...')
        elif p > escolhido:
            print('Menos...')
