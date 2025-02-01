try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except Exception as erro:
    #print(f'O problema encontrado foi {erro.__class__}{erro.__cause__}')
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito Obrigado!')
