# 1. Construa programa utilizando o comando condicional for para ler todos os n´umeros pares
# no intervalo de 1 a n. O valor de n deve ser digitado pelo teclado.

n = int(input('n = '))
print(f'Os números pares no intervalo de 1 a {n} são:')
for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=' ')
