# 5. Elabore um programa em que vocˆe entra com o valor do seu sal´ario l´ıquido e em seguida entre
# com a descri¸c˜ao “Descreva a 1ª despesa”(alimenta¸c˜ao, transporte, estudos, etc...), Ap´os isto
# apresentar uma mensagem para digitar o valor da despesa. Na medida em que lan¸ca a despesa
# ´e deduzida de seu saldo, e caso fique com um saldo negativo deve ser dada a mensagem, “Vocˆe
# estourou o seu limite, procure reorganizar o seu or¸camento”. Caso n˜ao queira lan¸car mais
# nenhuma despesa, responda N para a pergunta “Deseja lan¸car mais alguma despesa? S ou
# N : ”. Para N deve ser dado ao final a mensagem “Vocˆe ainda tem um saldo de R$xxx.xx

salario = float(input('Valor salário: '))
despesas = []
soma = 0

for i in range(1, despesas.len() +1):
    despesas.append(input('Despesa'))
