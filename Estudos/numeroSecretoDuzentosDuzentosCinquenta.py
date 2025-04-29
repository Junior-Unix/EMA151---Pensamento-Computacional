# 3. Elabore um programa em que a pessoa deve acertar o n´umero secreto, que deve ser gerado
# automaticamente e estar entre 200 e 250. A pessoa deve at´e 10 chances para tentar acertar,
# e a cada erro deve ser dada a indica¸c˜ao de“Tente novamente, o n´umero secreto ´e menor ou
# maior do que este. Vocˆe tem mais x tentativas”. Caso acerte deve ser dada a mensagem
# “Meus parab´ens vocˆe acertou na xa
# tentativa!”. E ainda caso n˜ao tenha conseguido deve ser
# dada a mensagem“Infelizmente vocˆe n˜ao tem mais tentativas. Fim de jogo”

import random

tentativas = 10

numeroAleatorio = random.randint(200, 250)

for i in range(1, tentativas):
    numeroInserido = int(input('Digite um numero entre [200] e [250]: '))
    if numeroInserido == numeroAleatorio and tentativas <= 10:
        print('Parabéns, seu número {} é o mesmo secreto {}'.format(numeroInserido, numeroAleatorio))
        break
    elif numeroInserido < numeroAleatorio:
        print('Seu numero {} é menor que u numero secreto'.format(numeroInserido))
        tentativas -= 1
    elif numeroInserido > numeroAleatorio:
        print('Seu numero {} é maior que o número secreto'.format(numeroInserido))
        tentativas -= 1
    elif tentativas == 10:
        print('{} tentativas atingidas'.format(tentativas))
    else:
        print('Você não acertou o número secreto, tente novamente')