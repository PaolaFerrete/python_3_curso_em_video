from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
if idade < 9:
    print('O Atleta tem {} anos'.format(idade))
    print('Classificação: MIRIM')
elif idade >= 9 and idade < 14:
    print('O Atleta tem {} anos'.format(idade))
    print('Classificação: INFANTIL')
elif idade >= 14 and idade < 19:
    print('O Atleta tem {} anos'.format(idade))
    print('Classificação: JUVENIL')
elif idade >= 19 and idade < 25:
    print('O Atleta tem {} anos'.format(idade))
    print('Classificação: SÊNIOR')
else:
    print('O Atleta tem {} anos'.format(idade))
    print('Classificação: MASTER')