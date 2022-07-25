try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com tipos de dados que você digitou')
except ZeroDivisionError:
    print(f'Não é possivel dividir um número por zero!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
except KeyboardInterrupt:
    print(f'O usuario preferiu não informar os dados!')

else:
    print(f'O resultado é  {r:.1f}')
finally:
    print(f'Volte sempre! Muito obrigado')