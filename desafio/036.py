cores = {'limpa':'\033[m', 'Amarelo': '\033[33m',
         'Branco':'\033[30m', 'Vermelho':'\033[31m',
         'Verde':'\033[32m', 'Azul':'\033[32m',
         'Roxo':'\033[35m', 'Azul Claro':'\033[36m',
         'Cinza':'\033[37m','Preto':'\033[7;30m'}
casa = float(input('Valor do Imóvel: '))
salario = float(input('Informe o salário: '))
ano = int(input('Total de prestação: '))
mes = ano * 12
prestaçao = casa / mes
por = (30 / 100) * salario
print('{}Processando...{}'.format(cores['Preto'], cores['limpa']))
print('A prestação mensal totalizando o valor de {}R${:.2f}{} por {}{}{} meses'.format(cores['Preto'],prestaçao,cores['limpa'],
                                                                                       cores['Preto'], mes, cores['limpa']))
if prestaçao <= por:
    print('{}Emprestimo CONCEDIDO{}'.format(cores['Preto'], cores['limpa']))
else: print('{}Emprestimo NEGADO{}'.format(cores['Vermelho'], cores['limpa']))

