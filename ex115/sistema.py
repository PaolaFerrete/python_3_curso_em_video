from ex115.lib.interface import *
from ex115.lib.arquivos import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
        #opção de listar o arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #cadastra uma pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mErro!Digite uma opção válida\033[m')
    sleep(2)