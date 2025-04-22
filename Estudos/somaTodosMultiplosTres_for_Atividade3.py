# 2. Construa programa utilizando o comando condicional for para obter a soma de todos os
# números múltiplos de três no intervalo de 1 a n. O valor de n deve ser digitado pelo teclado.

print('='*50)
print('Esse programa calcula a soma dos multiplos de "3" de 1 a n')
print('='*50)

n = int(input('Digite o valor para "n": '))
somaMultiplosTres = 0
for i in range(1, n+1):
    if i % 3 == 0:
        print('\033[1;32mMultiplo [{}]\033[0m'.format(i))
        somaMultiplosTres += i
print('A \033[1m{}{}\033[0m dos múltiplos de 3 de [1] a [{}] é: {}'.format('soma', '', n, somaMultiplosTres))