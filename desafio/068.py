from random import randint
soma = cont = 0
print('-==-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-==-'*30)
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = computador + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? ')).upper().strip()[0]
    print('-'*30)
    if soma % 2 == 0 and escolha == 'P':
        cont += 1
        print('Você jogou {} e o Computador {}. O total {} deu PAR'.format(jogador, computador, soma))
        print('Você Venceu!!!')
        print('Vamos jogar novamente!')
    elif soma % 2 == 1 and escolha == 'I':
        cont += 1
        print('Você jogou {} e o Computador {}. O total {} deu ÍMPAR'.format(jogador, computador, soma))
        print('Você Venceu!!!')
        print('Vamos jogar novamente!')
    else:
        break
print('Você Perdeu!')
print('-==-'*30)
print('GAME OVER! Você venceu {} vezes'.format(cont))