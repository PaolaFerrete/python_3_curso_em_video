from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year)
print('-=-'*30)
for k, v in trabalhador.items():
    print(f' - {k} tem o valor {v}')
