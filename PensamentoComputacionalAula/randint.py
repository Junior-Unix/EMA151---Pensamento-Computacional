# 4. Construa um programa utilizando a fun¸c˜ao randint da biblioteca random e o loop for para
# gerar n n´umeros inteiros entre os inteiros n1 e n2 a serem escolhidos pelo teclado

import random

# randon.randint(x,y)
while True:
    menu = input(f'Digite (c)ontinuar ou (s)air: ')
    if menu.lower() == 's':
        break
    n1 = int(input('Digite o valor de [n1]: '))
    n2 = int(input('Digite o valor de [n2]: '))
    limitador = int(input('Digite o valor de [limitador1]: '))
    for i in range(0, limitador):
        print(random.randint(n1, n2))