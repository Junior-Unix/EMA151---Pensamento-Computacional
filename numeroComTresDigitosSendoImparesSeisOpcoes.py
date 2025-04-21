# # Lista de dígitos disponíveis
# digitos = [0, 3, 5, 7, 8, 9]
#
# # Lista para armazenar os números válidos
# numeros_impares = []
#
# # Gerar combinações
# for unidade in [3, 5, 7, 9]:  # Dígitos das unidades devem ser ímpares
#     for centena in digitos:
#         if centena != unidade and centena != 0:  # A centena deve ser distinta e não pode ser 0
#             for dezena in digitos:
#                 if dezena != unidade and dezena != centena:  # A dezena deve ser distinta das demais
#                     # Formar o número
#                     numero = centena * 100 + dezena * 10 + unidade
#                     numeros_impares.append(numero)
#
# # Exibir os números gerados
# print("Números ímpares de três dígitos distintos:")
# print(numeros_impares)
# # Exibir a quantidade de números gerados
# print(f"Quantidade de números ímpares de três dígitos distintos: {len(numeros_impares)}")
# #  Exibir em ordem crescente os números gerados
# numeros_impares.sort()
# print(numeros_impares)
#


# Lista de dígitos disponíveis
digitos = [0, 3, 5, 7, 8, 9]

# Lista para armazenar os números válidos
numeros_impares = []

# Gerar combinações
for unidade in [3, 5, 7, 9]:  # Dígitos das unidades devem ser ímpares
    for centena in digitos:
        if centena != unidade and centena != 0:  # Centena distinta e não pode ser 0
            for dezena in digitos:
                if dezena != unidade and dezena != centena:  # Dezena distinta das demais
                    # Formar o número
                    numero = centena * 100 + dezena * 10 + unidade
                    numeros_impares.append(numero)

# Exibir os números gerados
print("Números ímpares de três dígitos distintos:")
print(numeros_impares)

# Exibir o total de números gerados
print(f"Total de números gerados: {len(numeros_impares)}")
