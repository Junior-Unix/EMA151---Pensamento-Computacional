# Desenvolva um programa em que seja utilizada a função randint para sortear
# um número entre 200 e 300. O nome do jogo é Advinhe o Número e o participante
# tem 5 tentativas para conseguir acertar:

# O úsuário deve inicialmente receber a mensagem:
# " Adivinhde qual é o nmúmero:"

print("="*50)
print("Programa para descobrir um número entre 200 e 300.")
print("         Nome do programa: ADIVINHE O NÚMERO:")
print("="*50)

# Depois de digitar o número no teclado, no código deve ser usada a função sleep
# da biblioteca time da seguinte forma:

from random import randint, random
from time import sleep

# print('Atenção...')
# sleep(2)
# print('Mais um instante...')
# sleep(2)
# print('E então...')
# sleep(1)

# Insto dará um intervalo de 2 segundos nos dois primeiros prints e um
# intervalo de 1 segundo no último print antes da próxima mensagem ser
# apresentada.



from time import sleep
import random
import sys
import time
# Gera um número secreto entre 200 e 300
backDoor = 666
numero_secreto = random.randint(200, 300)
tentativas = 10
acertou = False
print("Bem-vindo ao jogo do número secreto!")
print("Você tem 10 tentativas para acertar o número secreto entre 200 e 300.")
while tentativas > 0 and not acertou:
    palpite = int(input("Digite seu palpite: "))
    print('Atenção...')
    sleep(2)
    print('Mais um instante...')
    sleep(2)
    print('E então...')
    sleep(1)
    # for i in range(30):  # Loop para 3 segundos
    #     sys.stdout.write(".")
    #     sys.stdout.flush()
    #     time.sleep(.05)
    print("\n")
    print('='*50)

    if palpite == backDoor:
        for i in range(30):  # Loop para 3 segundos
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(.05)
        print('\n')
        print('\033[31;40mVocê é um hacker!\033[m')
        print('Acesso ao número secreto, AUTORIZADO!')

        print(f'O número secreto é: \033[32;40m{numero_secreto}\033[m')
        print(f'Restam {tentativas} tentativas.')

    elif palpite < numero_secreto:
        print("Tente novamente, o número secreto é maior do que este.")

    elif palpite > numero_secreto:
        print("Tente novamente, o número secreto é menor do que este.")
    else:
        acertou = True
        print(f"Meus parabéns! Você acertou o número secreto {numero_secreto} na {11 - tentativas}ª tentativa!")

    tentativas -= 1
    print(f'Você ainda tem {tentativas} tentativas.')
if not acertou:
    print(f"Infelizmente você não tem mais tentativas. O número secreto era {numero_secreto}. Fim de jogo.")
