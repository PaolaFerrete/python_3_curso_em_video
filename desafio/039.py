from datetime import date
atual = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = atual - ano
if idade == 18:
    print('Quem nasceu em {} tem {} em {}'.format(ano, idade, atual))
    print('Deve se alistar imediatamente!')
elif idade < 18:
    s = 18 - idade
    a = atual + s
    print('Quem nasceu em {} tem {} em {}'.format(ano, idade, atual))
    print('Ainda falta {} ano(s) para o alistamento'.format(s))
    print('Seu alistamento será em {}'.format(a))
else:
    s = idade - 18
    a = ano - s
    print('Quem nasceu em {} tem {} em {}'.format(ano, idade, atual))
    print('Deveria ter se alistado há {} anos'.format(s))
    print('Seu alistamento foi em {}'.format(a))