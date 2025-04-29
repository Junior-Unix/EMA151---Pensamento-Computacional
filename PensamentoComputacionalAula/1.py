from datetime import datetime

while True:
    print("="*32)
    print("SELEÇÃO OPORTUNIDADE DE TRABALHO")
    print("="*32)

    nome = input("Por favor, digite seu nome (ou 'q' para sair): ")
    if nome.lower() == 'q':
        break
    print(f'Olá, {nome.title()}!')
    ano_nascimento = int(input(f"Por gentiliza {nome.title()}, digite o ano em que você nasceu: "))

    # formações que possui:
    print("\nPor gentileza, marque a alternativa correspondente ao seu grau de formação:")
    print("0 - Cursando ensino médio:")
    print("1 - Ensino Médio:")
    print("2 - Cursando ensino superior:")
    print("3 - Ensino superior:")

    formacao = int(input("Por gentileza, digite uma das opções acima: "))
    print("")
    # Tempo de experiência na área de formação
    anos = int(input("Por favor digite o seu tempo de experiência na área de formação, em anos: "))

    # Quanto a fluência em inglês
    print("\nVocê é fluente em inglês?")
    print("1 - não.")
    print("2 - sim.")
    resposta = int(input("Por gentiliza, digite a opção que melhor se encaixa na sua resposta: "))

    # condições de classificação
    ano_corrente: int = datetime.now().year
    idade = ano_corrente - ano_nascimento
    experiencia = anos
    fluencia_ingles = 'sim' if resposta == 2 else 'não'

    # Dicionário com os dados do usuário
    user_data = {
        "nome": nome.title(),
        "ano_nascimento": ano_nascimento,
        "formacao": formacao,
        "experiencia": experiencia,
        "fluencia_ingles": fluencia_ingles
    }

    # Print the dictionary
    print("\nDados coletados:")
    for key, value in user_data.items():
        print(f"{key}: {value}")

    bold_green_black_start = "\033[1;32;40m"
    bold_end = "\033[0m"

    if idade > 30 and formacao == 3 and experiencia > 8 and fluencia_ingles == 'sim':
        print(f"{bold_green_black_start}{nome.title()}, siga para o atendimento até o 4º Andar e aguarde na sala 4A que será chamado pelo nome.{bold_end}")
    elif idade > 30 and formacao == 3 and experiencia <= 8 and fluencia_ingles == 'sim':
        print(f"{bold_green_black_start}{nome.title()}, siga para o atendimento até o 4º Andar e aguarde na sala 4B que será chamado pelo nome.{bold_end}")
    elif idade > 25 and formacao == 3 and experiencia > 2 and fluencia_ingles == 'sim':
        print(f"{bold_green_black_start}{nome.title()}, siga para o atendimento até o 3º Andar e aguarde na sala 3A que será chamado pelo nome.{bold_end}")
    elif idade > 25 and formacao == 3 and fluencia_ingles == 'não':
        print(f"{bold_green_black_start}{nome.title()}, siga para o atendimento até o 2º Andar e aguarde na sala 2B que será chamado pelo nome.{bold_end}")
    else:
        print(f"{bold_green_black_start}{nome.title()}, siga para o atendimento até o 1º Andar e aguarde ser chamado pelo nome.{bold_end}")