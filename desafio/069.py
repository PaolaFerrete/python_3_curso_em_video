print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)
contidade = contsexo = contmulher = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: ')).strip().upper()[0]
    if idade >= 18:
        contidade += 1
    if sexo == 'M':
        contsexo += 1
    if idade < 20 and sexo == 'F':
        contmulher += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Desaja continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}'.format(contidade))
print('Ao todo temos {} homens cadastrados'.format(contsexo))
print('E temos {} mulheres com menos de 20 anos'.format(contmulher))

