nomeAtleta = input("Atleta: ")
idadeAtleta = int(input("Idade: "))
#modalidadeAtleta = int(input("Modalidade: "))
print("\nEscolha a modalidade:")
print("1 - Natação:")
print("2 - Atletismo:")
print("3 - Outras:")
modalidadeAtleta = int(input("Digite sua modalidade: "))

if idadeAtleta >= 18:
    if modalidadeAtleta == 1:
        print(f"Olá atleta {nomeAtleta}, por favor, preencha o formulário para participar da seletiva.")
    elif modalidadeAtleta == 2:
        print(f" Olá atleta {nomeAtleta}, por favor, seguir para avaliação com o técnico.")
    elif modalidadeAtleta == 3:
        print(f"Olá atleta {nomeAtleta}, para a sua modalidade a seletiva será apenas em agosto.")
    else:
        print("Modalidade inválida!")

