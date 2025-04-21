# 1. Construa um programa utilizando o comando condicional for construir uma tabuada qualquer.

multiplicador = int(input("Digite o multiplicador para construção da tabuada: "))
i = 0
result = 0
for i in range(0,11):
    resultado = multiplicador * i
    print(f"{multiplicador} * {i} = {resultado}")