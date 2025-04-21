# PH da água
ph = input("Digite o valor do pH da solução: ")

ph = float(ph)

# Determina a classificação da solução com base no pH
if ph < 7:
    print("A solução é ácida.")
elif ph == 7:
    print("A solução é neutra.")
elif ph > 7:
    print("A solução é básica.")
else:
    print("Valor de pH inválido.")
