nome = input('Qual é o seu nome? ')
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
print('Tenha um bom dia, {}'.format(nome))