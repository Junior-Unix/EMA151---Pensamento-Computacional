# 4. Trˆes n´umeros inteiros quaisquer devem ser digitados pelo teclado como sendo A, B e C. O
# programa deve mostr´a-los em ordenadamente.

a = int(input('Digite o primeiro número para "A": '))
b = int(input('Digite o segundo número para "B": '))
c = int(input('Digite o terceiro número para "C": '))

# Ordena os números A, B e C
numeros = [a, b, c]
numeros.sort()
menor, meio, maior = numeros

print(f'Os números em ordem crescente são: {menor}, {meio} e {maior}.')


