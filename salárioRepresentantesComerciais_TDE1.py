# 2. (RA1) Precisamos calcular os sal´ arios dos representantes comerciais de uma de
# terminada empresa. Eles recebem um valor fixo de R$1800,00 e 6% de comiss˜ ao
#  sobre as vendas realizadas. Considere que os representantes Jos´ e, Claudio e
#  Ana fecharam o mˆ es com R$12.398,00, R$15.745,00 e R$18.732,00 em vendas res
# pectivamente. Descreva cada etapa necess´ aria para a resolu¸c˜ ao do problema,
#  n˜ ao ´ e necess´ ario fazer o programa, apenas descrever cada uma das etapas que
#  permitiram aplicar o pensamento computacional na resolu¸c˜ao do problema.

# 1. Ler os dados de entrada: vendas dos representantes
vendas = {
    "Jose": 12398.00,
    "Claudio": 15745.00,
    "Ana": 18732.00
}

# 2. Definir o salário fixo e a porcentagem de comissão
salario_fixo = 1800.00
comissao_porcentagem = 0.06
# 3. Calcular o salário total para cada representante
salarios = {}
for representante, venda in vendas.items():
    comissao = venda * comissao_porcentagem
    salario_total = salario_fixo + comissao
    salarios[representante] = salario_total

# 4. Exibir os resultados
for representante, salario in salarios.items():
    print(f"\033[32;40mSalário de {representante}: R$ {salario:.2f}\033[m")
# 5. Salvar os resultados em um arquivo
with open("salarios_representantes.txt", "w") as arquivo:
    for representante, salario in salarios.items():
        arquivo.write(f"Salário de {representante}: R$ {salario:.2f}\n")
# 6. Finalizar o programa
print("Cálculo de salários concluído.")
# 7. Encerrar o programa
print("Programa encerrado.")
# 8. Fim do programa
def calcular_salario(vendas, salario_fixo=1800.00, comissao_porcentagem=0.06):
    comissao = vendas * comissao_porcentagem
    return salario_fixo + comissao

def main():
    representantes = {}
    while True:
        nome = input("Digite o nome do representante (ou '(q)uit' para encerrar): ")
        if nome.lower() == 'q':
            break
        vendas = float(input(f"Digite o valor das vendas de {nome}: "))
        representantes[nome] = vendas

    salarios = {nome: calcular_salario(vendas) for nome, vendas in representantes.items()}

    with open("salarios_representantes.txt", "w") as arquivo:
        for nome, salario in salarios.items():
            arquivo.write(f"Salário de {nome}: R$ {salario:.2f}\n")

    print("Cálculo de salários concluído.")
    for nome, salario in salarios.items():
        print(f"Salário de {nome.title()}: R$ {salario:.2f}")
    print("Programa encerrado.")

if __name__ == "__main__":
    main()