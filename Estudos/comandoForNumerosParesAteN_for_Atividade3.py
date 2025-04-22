# 1. Construa programa utilizando o comando condicional for para ler todos os números pares
# no intervalo de 1 a n. O valor de n deve ser digitado pelo teclado.

print('='*50)
print('Esse programa lê todos os numeros pares de 1 a n')
print('='*50)

n = int(input('Digite o valor de n: '))
print('Os números pares de 1 a [{}] são:'.format(n))
for i in range(1, n+1):
    if n % 2 == 0:
        print(i, end=' ')
