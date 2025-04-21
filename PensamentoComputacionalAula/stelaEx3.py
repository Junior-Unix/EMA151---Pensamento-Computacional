# Script para classificação e encaminhamento de candidatos

# Entrada de dados
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
formacao = int(input("Escolha sua formação (0: Cursando Ensino Médio, 1: Ensino Médio, 2: Cursando Curso Superior, 3: Curso Superior): "))
experiencia = int(input("Digite o tempo de experiência na área de formação (em anos): "))
ingles = input("Você é fluente em inglês? (1: sim, 2: não): ")

# Calculando idade
ano_atual = 2025
idade = ano_atual - ano_nascimento

# Classificação e encaminhamento
if idade > 30 and formacao == 3:
    if experiencia > 8 and ingles.lower() == "sim":
        print(f"{nome}, siga para atendimento até o 4º Andar e aguarde na sala 4A.")
    elif experiencia <= 8 and ingles.lower() == "sim":
        print(f"{nome}, siga para atendimento até o 4º Andar e aguarde na sala 4B.")
elif idade > 25 and formacao == 3:
    if experiencia > 2 and ingles.lower() == "sim":
        print(f"{nome}, siga para atendimento até o 3º Andar e aguarde na sala 3A.")
    elif ingles.lower() != "sim":
        print(f"{nome}, siga para atendimento até o 2º Andar e aguarde na sala 2B.")
else:
    print(f"{nome}, siga para atendimento até o 1º Andar e aguarde ser chamado.")

# Fim do script
