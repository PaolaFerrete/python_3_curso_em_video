jogador = dict()
partidas = list()
cont = 0
jogador['nome'] = str(input('Nome do jogador: '))
numero = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for v in range(0, numero):
    partidas.append((int(input(f'    Quantos gols na partida {v}: '))))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=-'*30)
print(jogador)
print('-=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i}, fez {v} gols. ')
print(f'Foi um total de {jogador["total"]} gols')
