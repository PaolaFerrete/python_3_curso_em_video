dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] >= 7.0:
    dados['resultado'] = 'Aprovado'
elif dados['media'] <= 7.0 and dados['media'] >= 5.0:
    dados['resultado'] = 'Recuperação'
#elief 7.0 dados 
else:
    dados['resultado'] = 'Reprovado'
print('-=-'*30)
for k, v in aluno.items()
    print(f' - {k} é igual a {v}')