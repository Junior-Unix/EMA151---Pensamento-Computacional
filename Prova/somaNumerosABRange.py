# 1. Usar a instrução for e if para realizar a soma de todos os números de A até B
# de acordo com as respostas abaixo apresentadas. Utilize a função range e entre pelo teclado
# com os valores de A e de B, sendo A menor que B. Ao final o programa deve apresentar os seguintes
# resultados:
#     A soma de todos os números inteiros de A e B é igual a XXX
#     A soma de todos os números inteiros de A a B que são multiplos de 5 é igual a XXX

print('='*50)
print('Esse programa soma todos os inteiros de A a B.')
print('='*50)


# A = int(input('Digite o valor de A: '))
# B = int(input('Digite o valor de B :'))
# for i in range(A, B+1):
#     if A > B:
#         A = int(input('A não pode ser maior que B, digite novamente o valor de A: '))
#     elif A <= B:
#         A =+ A
#         print('{}'.format(A))


print('Esse programa calcula a soma dos multiplos de "5" de 1 a n')

A = int(input('Digite o valor de A: '))
n = int(input('Digite o valor para o Limitador [B]: '))

soma = 0
for i in range(A, n+1):
    if i % 5 == 0:
        soma += i

print(f'A soma dos multiplos de 5 de {A} a {n} é igual a: {soma}')
print('='*20)

soma = 0
for i in range(A, n+1):
    soma += i
print(f'A soma de {A} a {n} é igual a: {soma}')
print('=' * 20)
