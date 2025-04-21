while True:
    print("="*19)
    print("SELETIVA DE ATLETAS")
    print("="*19)

    # ENTRADA DE DADOS
    nome = input("Por favor, digite seu nome (ou 'q' para sair): ")
    if nome.lower() == 'q':
        break
    print(f"Oi, {nome.title()}!")
    idade = int(input("Por gentiliza, digite sua idade: "))

    print("\nEscolha a modalidade:")
    print("1 - Natação:")
    print("2 - Atletismo:")
    print("3 - Outras:")
    modalidade = int(input("Digite sua modalidade: "))

    # condições de cada modalidade
    if idade >= 18:
        if modalidade == 1:
            print(f"Olá atleta {nome.title()}, por favor, preencha o formulário para participar da seletiva.")
        elif modalidade == 2:
            print(f" Olá atleta {nome.title()}, por favor, seguir para avaliação com o técnico.")
        elif modalidade == 3:
            print(f"Olá atleta {nome.title()}, para a sua modalidade a seletiva será apenas em agosto.")
        else:
            print("Modalidade inválida!")
    else:
        print("Poxa, que pena! Para participar das seletivas é preciso ter no mínimo '18' anos.")