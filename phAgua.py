while True:
    # Solicita ao usuário o valor do pH
    ph_input = input("Digite o valor do pH da solução (ou 'q' para sair): ")
    if ph_input.lower() == 'q':
        break
    ph = float(ph_input)

    # Determina a classificação da solução com base no pH
    if ph < 7:
        print("A solução é ácida.")
    elif ph == 7:
        print("A solução é neutra.")
    elif ph > 7:
        print("A solução é básica.")
    else:
        print("Valor de pH inválido.")
