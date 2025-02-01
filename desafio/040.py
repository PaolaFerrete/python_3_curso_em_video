n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Tirando {} e {} a média do aluno é de {}'.format(n1, n2, m))
    print('O aluno está reprovado')
elif m >= 5.0 and m <= 6.9:
    print('Tirando {} e {} a média do aluno é de {}'.format(n1, n2, m))
    print('O aluno está de recuperação')
elif m >= 7:
    print('Tirando {} e {} a média do aluno é de {}'.format(n1, n2, m))
    print('O aluno está de aprovado')

