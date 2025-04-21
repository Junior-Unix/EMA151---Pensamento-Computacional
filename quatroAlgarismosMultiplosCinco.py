# Quantos números múltiplos de cinco com quatro algarismos distintos podem ser formados
# com os algarismos 0, 1, 2, 3, 4, 5, 6?

from itertools import permutations

# Algarismos disponíveis
algarismos = ['0', '1', '2', '3', '4', '5', '6']

# Função para verificar se um número é múltiplo de 5
def eh_multiplo_de_cinco(numero):
    return int(numero) % 5 == 0

# Gerar todas as permutações de 4 algarismos
permutacoes = permutations(algarismos, 4)

# Filtrar permutações que são múltiplos de 5 e não começam com 0
multiplos_de_cinco = [''.join(p) for p in permutacoes if eh_multiplo_de_cinco(''.join(p)) and p[0] != '0']

# Exibir a quantidade de números múltiplos de cinco com quatro algarismos distintos
print(len(multiplos_de_cinco))
# Abrir arquivo para escrita
with open("resultados_multiplos_de_cinco.txt", "w") as arquivo:
    # Escrever cada múltiplo de cinco no arquivo
    for numero in multiplos_de_cinco:
        arquivo.write(numero + "\n")

# Exibir a quantidade de números múltiplos de cinco com quatro algarismos distintos
print(len(multiplos_de_cinco))
