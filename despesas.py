# 5. Elabore um programa em que vocˆe entra com o valor do seu sal´ario l´ıquido e em seguida entre
# com a descri¸c˜ao “Descreva a 1ª despesa”(alimenta¸c˜ao, transporte, estudos, etc...), Ap´os isto
# apresentar uma mensagem para digitar o valor da despesa. Na medida em que lan¸ca a despesa
# ´e deduzida de seu saldo, e caso fique com um saldo negativo deve ser dada a mensagem, “Vocˆe
# estourou o seu limite, procure reorganizar o seu or¸camento”. Caso n˜ao queira lan¸car mais
# nenhuma despesa, responda N para a pergunta “Deseja lan¸car mais alguma despesa? S ou
# N : ”. Para N deve ser dado ao final a mensagem “Vocˆe ainda tem um saldo de R$xxx.xx

print('Este programa calcula despesas debitando do salário líquido.')

salarioLiquido = float(input('Digite o valor do seu salário líquido: '))
despesas = []
saldo = salarioLiquido
continuar = 'S'
while continuar.upper() == 'S':
    nome_despesa = input('Digite o nome da despesa: ')
    valor_despesa = float(input('Digite o valor da despesa: '))
    despesas.append({'nome': nome_despesa, 'valor': valor_despesa})
    saldo -= valor_despesa
    if saldo < 0:
        print('Você estourou o seu limite, procure reorganizar o seu orçamento.')
    continuar = input('Deseja lançar mais alguma despesa? S ou N: ')

print(f'Você ainda tem um saldo de R${saldo:.2f}')
print('Despesas:')
for despesa in despesas:
    print(f"{despesa['nome']}: R${despesa['valor']:.2f}")
print(f'Saldo restante: R${saldo:.2f}')
print('='*20)