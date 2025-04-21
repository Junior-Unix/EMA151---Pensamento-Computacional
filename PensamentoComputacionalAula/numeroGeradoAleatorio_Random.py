import random
# 5. Pesquisar na documenta¸c˜ ao do python, encontrar a biblioteca random e verificar
 # qual ´ e a fun¸c˜ ao que possibilita gerar um valor inteiro aleatoriamente. Depois disso
 # construa um programa que imprime um valor inteiro gerado aleatoriamente. A
 # mensagem na tela deve ser a seguinte:
 # O n´ umero gerado aleatoriamente ´e xxxx.


while True:
    numero_aleatorio = random.randint(0, 100)
    print(f"\033[32;40mO número gerado aleatoriamente é {numero_aleatorio}.\033[m")
    if input("Pressione 'q' para sair ou 'ENTER'' para gerar outro número: ").lower() == 'q':
        break

