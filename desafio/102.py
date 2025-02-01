def fatorial(n=1, show=False):
    """
    -> Calcula a farotial (n, show=False)
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do fatorial do número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)