# TRATAMENTO DE EXCESSAO
# TRY - EXCEPT
while True:
    print("="*32)
    if input("Digite 'q' para sair ou qualquer tecla para continuar: ").lower() == 'q':
        break
    try:
        # Código que pode gerar uma exceção
        x = int(input('x = '))
        y = int(input('y = '))
        resultado = x / y
        print(f'O valor de x é {x} e o valor de y é {y}.')
    except ValueError:
        print(f'Entrada inválida. Por favor, insira um número inteiro.')
    except ZeroDivisionError:
        print(f'Não é possível dividir por zero.')
    else:
        print(f'Os valores de x e y foram lidos corretamente: {x} e {y}.')
    finally:
        print('='*32)
# except ValueError:
# x = int(input('x = '))
# y = int(input('y = '))
# print(f'O valor de x é {x} e o valor de y é {y}.')
