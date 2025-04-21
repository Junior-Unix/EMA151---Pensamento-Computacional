# COMANDO CONDICIONAL IF
# ======================
# EXEMPLO 1
#
# idade = int(input('Por favor qual sua idade? '))
#
# if idade > 17:
#     print('Dirija-se ao guiche 8  e adquira o seu ingresso. Tenha um bom filme.')
# else:
#     print('Infelizmente este filme não é para menores.')

# Equação do segundo grau, raizes reais.
# Δ > 0 => 2 raizes reais e diferentes
# Δ = 0 => 2 reizes reais e iguais
# Δ < 0 => não terá raizes reais.

print('Digite os valores de a, b e c')

a = int(input('Digite o valor de "a": '))
b = int(input('Digite o valor de "b": '))
c = int(input('Digite o valor de "c": '))

delta = int(b**2-(4*a*c))

print('='*30)
print(f'O valor de delta é igual a: {delta}.')
print('='*30)

# print(delta)

if delta > 0:
    print('2 raizes reais e diferentes')
elif delta == 0:
    print('2 raizes reais e iguais.')
elif delta < 0:
    print('Não tem raizes Reais.')

