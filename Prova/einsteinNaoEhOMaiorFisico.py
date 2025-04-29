# Escreva um programa que utilize a instrução while para que seja respondida a
#     pergunta: Quem é considerado o maior Físico de todos os tempos? O programa
# deve encerrar apenas quando a resposta for correta e com a seguinte frase:
#     Meus parabéns! Você acertou! Einstein tem como legado mais proeminente a teoria
#     da relatividade e é considerado o maior de todos os tempor!!!

print('Esse programa informa por coerção quem é o maior Físico de todos os tempos:')

fisico = 'Einstein'

while True:
    resposta = input('Quem é considerado o maior Físico de todos os tempos? \nR.:')
    if resposta != 'Einstein':
        print('Tente novamente: ')
    elif resposta == 'Einstein':
        print('Você acertou! Einstein tem como legado mais proeminente a teoria da relatividade e é considerado o maior de todos os tempor!!!')
        break
