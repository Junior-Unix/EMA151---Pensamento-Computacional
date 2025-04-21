#Título.
print(f"="*36)
print(f"Organizador de Despesas Financeiras!")
print(f"="*36)

#Recebimento de dados.
nome = input(f"Olá! Para começarmos a calcular suas despesas, digite o seu nome: ").capitalize()
salario = float(input(f"{nome}, digite o seu salário líquido total:"))
despesa = 0
ad = input(f"{nome}, você deseja incluir alguma despesa neste mês? Se sim digite 'S', se não digite 'N'").capitalize()

#Tratamento de dados e recebimento de despesas.
if ad == "S":
    despesasnome = []
    despesasvalor = []
    while ad == "S":
       if sum(despesasvalor) < salario:
         nomed = input(f"Digite o nome da despesa a ser adicionada: ")
         despesasnome.append(nomed)
         valord = int(input(f"Digite o valor gasto em '{nomed}:"))

         despesasvalor.append(valord)
         ad = input(f"Você deseja adicionar mais alguma despesa? Se sim digite 'S', se não digite 'N'").capitalize()
       else:
            print(f"{nome}, você estourou o seu limite. Procure reorganizar seu orçamento!")
       break
       somad = sum(despesasvalor)
       print("")
       print(f"A sua lista despesas deste mês é: {despesasnome}.")
       print(f"A soma de seus gastos é de {somad}")
       print(f"Portanto você ainda tem o saldo de R${salario - somad}!")
        #else:
#    print("")

print(f"Já que não há nenhuma despesa, seu salário líquido é: R${salario}")