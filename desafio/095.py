jogador = dict()
ngols = list()
total = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, partidas + 1):
        ngols.append(int(input(f'    Quantos gols na partida {p}? ')))
    jogador['gols'] = ngols[:]
    jogador['total'] = sum(ngols)
    ngols.clear()
    total.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Por favor, responda S ou N')
    if resp in 'N':
        break
print('-=-' * 30) #cabeçalho
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(total):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar os dados de qual jogador? [999 interrompe]'))
    if busca == 999:
        break
    if busca >= len(total):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {total[busca]["nome"]}')
        for i, g in enumerate(total[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)