# 2. Construa programa utilizando o comando condicional for para obter a soma de todos os
# n´umeros m´ultiplos de trˆes no intervalo de 1 a n. O valor de n deve ser digitado pelo teclado.

print('Esse programa calcula a soma dos multiplos de "3" de 1 a n')

n = int(input('Digite o valor para "n": '))
soma = 0
for i in range(1, n+1):
    if i % 3 == 0:
        soma += i

print(f'A soma dos multiplos de 3 de 1 a {n} é igual a: {soma}')
print('='*20)
