from datetime import datetime

# 3. Numa empresa de empregos ao chegar na recepção o intereçado em buscar
# uma oportunidade de trabalho responde as seguintes questões:
# - Nome:
# - Ano de nascimento:
# - Formação que tem as opções: cursando ensino médio (0)
#                               ensino mécio          (1)
#                               cursando superior     (2)
#                               curso superior        (3)
# - Tempo de experiência na área de formação ( em anos)
# - Flueência em inglês
#
# Escrever um script que leia os dados de entrada pelo teclado, classifique
# e encaminhe o interessado para ser atendido, conforme segue:
#
# - Maior de 340 anos com opção 3, mais de 8 anos de experiência e fluencia em
# inglês - Siga para o atendimento até o 4º Andar e aguarde na sala 4A que será
# chamado pelo nome.
#  - Maior de 30 anos com opção 3, menos de 8 anos de esperiência e com fluência
#  em inglês - Siga para o atendimento até o 4º Andar e aguarde na sala 4B que 
# será chamado pelo nome.
# - Maior de 25 anos, opção 3, mais de 2 anos de experiência e fluênte em inglês -
# Siga para atendimento até o 3º Andar e aguarde na sala 3A que será chamado pelo
# nome.
# - Maior de 25 anos, opção 3, sem fluência em inglês - Siga para atendimento até
# o 2º Andar e aguarde na sala 2B que será chamado pelo nome.
# - Demais casos - Siga para atendimento até o 1º Andar e aguarde ser chamado pelo
# nome.


# - Nome:
# - Ano de nascimento:
# - Formação que tem as opções: cursando ensino médio (0)
#                               ensino mécio          (1)
#                               cursando superior     (2)
#                               curso superior        (3)
# - Tempo de experiência na área de formação ( em anos)
# - Flueência em inglês

nome = str(input("Digite seu nome: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
formacao = int(input("Digite sua formação (0 - cursando ensino médio, 1 - ensino médio, 2 - cursando superior, 3 - curso superior): "))
experiencia = int(input("Digite seu tempo de experiência na área de formação (em anos): "))
fluencia_ingles = str(input("Você é fluente em inglês? (s/n): "))

# Escrever um script que leia os dados de entrada pelo teclado, classifique
# e encaminhe o interessado para ser atendido, conforme segue:
#
#  - Maior de 30 anos com opção 3, menos de 8 anos de esperiência e com fluência
#  em inglês - Siga para o atendimento até o 4º Andar e aguarde na sala 4B que 
# será chamado pelo nome.
# - Maior de 25 anos, opção 3, mais de 2 anos de experiência e fluênte em inglês -
# Siga para atendimento até o 3º Andar e aguarde na sala 3A que será chamado pelo
# nome.
# - Maior de 25 anos, opção 3, sem fluência em inglês - Siga para atendimento até
# o 2º Andar e aguarde na sala 2B que será chamado pelo nome.
# - Demais casos - Siga para atendimento até o 1º Andar e aguarde ser chamado pelo
# nome.

# Essa função calcula tempo cronológico a partir da data do computador.
# O professor não ensinou ainda, pequei no livro que estou estudando.
current_year = datetime.now().year
idade = current_year - ano_nascimento

if idade > 30 and formacao == 3 and experiencia > 8 and fluencia_ingles.lower() == 's':
    print(f"{nome}, siga para o atendimento até o 4º Andar e aguarde na sala 4A que será chamado pelo nome.")
elif idade > 30 and formacao == 3 and experiencia <= 8 and fluencia_ingles.lower() == 's':
    print(f"{nome}, siga para o atendimento até o 4º Andar e aguarde na sala 4B que será chamado pelo nome.")
elif idade > 25 and formacao == 3 and experiencia > 2 and fluencia_ingles.lower() == 's':
    print(f"{nome}, siga para o atendimento até o 3º Andar e aguarde na sala 3A que será chamado pelo nome.")
elif idade > 25 and formacao == 3 and fluencia_ingles.lower() == 'n':
    print(f"{nome}, siga para o atendimento até o 2º Andar e aguarde na sala 2B que será chamado pelo nome.")
else:
    print(f"{nome}, siga para o atendimento até o 1º Andar e aguarde ser chamado pelo nome.")


