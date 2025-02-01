#adicionar elementos
dados = {'nome':'Pedro', 'idade': 25}
print(dados)
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'm'
print(dados['sexo'])
#deletar elementos
del dados['idade']
print(dados)
# imprimir elementos
filme = {'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas',
         }
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
#junção entre lista, túpla e dicionário
locadora = []
filme1 = {'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas',
         }
filme2 = {'título': 'Avengers',
         'ano': '2012',
         'diretor': 'Joss Whedon'}
locadora.append(filme1.copy())
locadora.append(filme2.copy())
print(locadora)

#Prática 1
pessoas = {'nome': 'Gustavo', 'sexo': 'm', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5

#Prática 2: criando um dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])

#Prática 3
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v)