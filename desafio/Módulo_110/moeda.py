def aumentar(preço=0, taxa=0, formato=False):
        res = preço + (preço * taxa / 100)
        return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
        res = preço - (preço * taxa / 100)
        return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
        res = preço * 2
        return res if not formato else moeda(res) #outra forma de fazer


def metade(preço=0, formato=False):
        res = preço / 2
        return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
        return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaAu=10, taxaDi=5):
        print('-' * 40)
        print('RESUMO DO VALOR'.center(40))
        print('-' * 40)
        print(f'Preço analisado: \t\t{moeda(preço)}')
        print(f'Metade do preço:  \t\t{(metade(preço, True))}')
        print(f'Dobro do preço: \t\t{(dobro(preço, True))}')
        print(f'{taxaAu}% de aumento: \t\t{(aumentar(preço, taxaAu, True))}')
        print(f'{taxaDi}% de redução:  \t\t{(diminuir(preço, taxaDi, True))}')