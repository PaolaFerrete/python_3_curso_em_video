"""Meu programa
def notas(*num, sit=False):
    notas(*num, sit=False)
    -> Função para analisar notas e situação dos alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações da turma

    total = len(num)
    maior = num[0]
    menor = num[0]
    soma = media = 0
    situacao = ''
    dicionario = dict()
    for valor in num:
        soma += valor
        if maior < valor:
            maior = valor
        if menor > valor:
            menor = valor
    media = soma / len(num)
    dicionario = {'total': total, 'maior': maior,
                  'menor': menor, 'media': media}
    if sit:
        if media >= 7:
            situacao = 'Boa'
        elif media < 7 and media >= 5:
            situacao = 'Regular'
        else:
            situacao = 'Ruim'
        dicionario = {'total': total, 'maior': maior,
                  'menor': menor, 'media': media,
                  'situação': situacao}
    return dicionario



#programa principal
resp = notas(7.0, 6.0, 6.5, sit=True)
print(resp)
help(notas)"""

#Programa Guanabara
def notas(*n, sit=False):
    """
    notas(*num, sit=False)
    -> Função para analisar notas e situação dos alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#programa principal
resp = notas(7.0, 6.0, 6.5, sit=True)
print(resp)
help(notas)

