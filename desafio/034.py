s = float(input('Digite o valor do seu salário: '))
if s > 1250:
    ns = (10 / 100) * s + s
    print('O seu novo salário com aumento de 10% será {:.2f}'.format(ns))
else:
    ns = (15 / 100) * s + s
    print('O seu novo salário com aumento de 15% será {:.2f}'.format(ns))