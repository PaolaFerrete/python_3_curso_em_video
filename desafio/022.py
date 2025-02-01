#analisador de texto
nome = str(input('Digite seu nome completo: '))
print('analisado seu nome...')
print('o seu nome em maiúsculas é {}'.format(nome.upper()))
print('o seu nome e minúsculas é {}'.format(nome.lower()))
print('seu nome ao todo tem {}'.format(len(nome) - nome.count(' ')))
print('seu primerio nome tem {} letras'.format(nome.find(' ')))
