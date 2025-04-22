# 3. Elabore um programa em que a pessoa deve acertar o número secreto, que deve ser gerado
# automaticamente e estar entre 200 e 250. A pessoa deve até 10 chances para tentar acertar,
# e a cada erro deve ser dada a indicação de“Tente novamente, o número secreto é menor ou
# maior do que este. Vocˆe tem mais x tentativas”. Caso acerte deve ser dada a mensagem
# “Meus parabéns você acertou na xª tentativa!”. E ainda caso não tenha conseguido deve ser
# dada a mensagem“Infelizmente você não tem mais tentativas. Fim de jogo”

print('='*50)
print('Programa para descobrir um número entre 200 e 250')
print('='*50)

# Importando as bibliotecas necessárias
import random

# Gera um número secreto entre 200 e 250
numeroSecreto = random.randint(200,250)
tentativas = 10
#acertou = False

print('Bem-vindo ao jogo do número secreto!')
while True:

    entrada = input('Digite um numero entre 200 e 250: ')
    if not entrada.isdigit():
        print('ENTER é entrada inválida! Por favor, insira um número entre 200 e 250.')
        continue
    numeroInserido = int(entrada)

#    numeroInserido = int(input('Digite um numero entre 200 e 250: '))

    if numeroInserido == numeroSecreto:
        print('\033[1:32;40mMeus parabéns! Você acertou o número secreto na {} tentativa!\033[m'.format(tentativas))
        tentativas -= 1
    elif numeroInserido < numeroSecreto:
        print('O numero inserido é menor que o número secreto, vc tem mais {} tentativas'.format(tentativas))
        tentativas -= 1
    elif numeroInserido > numeroSecreto:
        print('O número inserido é maior que o número secreto, vc tem mais {} etntativas'.format(tentativas))
        tentativas -= 1
    elif tentativas == 0:
        print('Infelizmente vc não tem mais tentativas, o número secreto era {}'.format(numeroSecreto))
        break


# Tentativa de anular o ENTER no lugar do número inserido
# pra não crashar o programa.
# entrada = input('Digite um numero entre 200 e 250: ')
#     if not entrada.isdigit():
#         print('Entrada inválida! Por favor, insira um número entre 200 e 250.')
#         continue
#     numeroInserido = int(entrada)