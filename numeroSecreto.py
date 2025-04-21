# 3. Elabore um programa em que a pessoa deve acertar o n´umero secreto, que deve ser gerado
# automaticamente e estar entre 200 e 250. A pessoa deve at´e 10 chances para tentar acertar,
# e a cada erro deve ser dada a indica¸c˜ao de“Tente novamente, o n´umero secreto ´e menor ou
# maior do que este. Vocˆe tem mais x tentativas”. Caso acerte deve ser dada a mensagem
# “Meus parab´ens vocˆe acertou na xa
# tentativa!”. E ainda caso n˜ao tenha conseguido deve ser
# dada a mensagem“Infelizmente vocˆe n˜ao tem mais tentativas. Fim de jogo”


import random
from time import sleep

# Gera um número secreto entre 200 e 250
numero_secreto = random.randint(200, 250)
tentativas = 10
acertou = False
print("Bem-vindo ao jogo do número secreto!")
print("Você tem 10 tentativas para acertar o número secreto entre 200 e 250.")
while tentativas > 0 and not acertou:

    print(f"\nVocê ainda tem {tentativas} tentativas.")
    palpite = int(input("Digite seu palpite: "))
    print('Atenção...')
    sleep(2)
    print('Mais um instante...')
    sleep(2)
    print('E então...')
    sleep(1)

    if palpite < numero_secreto:
        print("Tente novamente, o número secreto é maior do que este.")
    elif palpite > numero_secreto:
        print("Tente novamente, o número secreto é menor do que este.")
    else:
        acertou = True
        print(f"Meus parabéns! Você acertou o número secreto {numero_secreto} na {11 - tentativas}ª tentativa!")

    tentativas -= 1
if not acertou:
    print(f"Infelizmente você não tem mais tentativas. O número secreto era {numero_secreto}. Fim de jogo.")
