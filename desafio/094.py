banco = []
dados = dict()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print('ERRO! por favor, responda F ou M.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    banco.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! por favor, responda F ou M.')
    if resp == 'N':
        break
print(f'Ao todo temos {len(banco)} pessos cadastradas')
media = soma/len(banco)
print(f'A media de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in banco:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}  ', end='')
print()
print('Lista das pessoas que estão acima da média: ', end='')
for p in banco:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<<< ENCERRADO >>>')

