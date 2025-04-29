# Três números inteiros quaisquer devem ser digitados pelo teclado como sendo A, B e C.
# O programa deve mostrá-los ordenadamente.

# numeros = []
# numeros.append(int(input('Valor de A: ')))
# numeros.append(int(input('Valor de B: ')))
# numeros.append(int(input('Valor de C: ')))
#
# numeros.sort()
# print('Os números digitados em ordem são: {}'.format(numeros))

numeros = []

numeros.append(int(input('A: ')))
numeros.append(int(input('B: ')))
numeros.append(int(input('C: ')))

numeros.sort()

print('{}'.format(numeros))