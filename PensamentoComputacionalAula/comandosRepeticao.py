# COMANDO DE REPETIÇÃO (for)

for i in range(10):
    print("Bom dia")

print("="*20)

for i in range(10):
    print(i)

print("="*20)

for i in range(1, 4):
    print(i)

print("="*20)

for i in range(1,41):
    if i % 2 == 0:
        print(i)

print("="*20)

for i in range(1, 41):
    if i % 2 == 0 and i > 7:
        print(i)

soma = 0

print("="*20)

for i in range(1, 41):
    soma += i

print(f'o valor de total de soma é {soma}')

print("="*20)

n = int(input('Digite um valor inteiro positivo: '))
soma = 0

for i in range(1, n + 1):
    soma += i
print(f'A soma dos inteiro de 1 até "n" {n} é igual a {soma}.')

print("="*20)

# WHILE

n = int(input('Digite um valor positivo: '))
soma = 0
i = 1
while i <= n:
    soma += i
    i += 1

print(f'A soma dos inteiro de 1 até "n" {n} é igual a {soma}.')

print("="*20)

n = int(input('Digite um vaor positivo: '))
soma = 0
i = 1
while True:
    soma += i
    if soma == n:
        print(f'A soma de 1 até {n} é igual a soma {soma}.')
        break

print("="*20)

nome =  'Mozart'
while True:
    nome2 = input('Digite um nome: ').capitalize()
    if nome2 == nome:
        print(f'Meus parabéns, você acertou !!!')
        break
    else:
        print('Tente novamente')

print("="*20)

num = 40
while True:
    valor = int(input('Qual é o número? '))
    if valor == num:
        print('Meus parabéns, você ganhou o prêmio!!!')
        break
    else:
        print('Infelizmente não foi desta vez!!!')

