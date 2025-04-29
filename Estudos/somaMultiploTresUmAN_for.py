# 2. Construa programa utilizando o comando condicional for para obter a soma de todos os
# n´umeros m´ultiplos de trˆes no intervalo de 1 a n. O valor de n deve ser digitado pelo teclado.

n = int(input('Digite o limitador para somar todos os numeros multiplos de tres: '))
soma = 0
for i in range(1, n+1):
    if i % 3 == 0:
        soma += i
        print('{} é múltiplo de tres e a soma está em: {}.'.format(i, soma))

print('A soma dos multiplos de tres de um até {} é: {}'.format(n, soma))
