# 3. Utilize o bloco if - elif - else, para verificar a permissão de acesso ao digitar a idade:
# a) idade maior ou igual a 18 anos "Acesso Permitido"
# b) Idade maior ou igual a 12 anos e menor do que 18 anos "Acesso necessita autorização de um administrador"
# c) Idade menor 12 anos "Acesso negado"

print('='*50)
print("Esse programa verifica a permissão de acesso ao digitar a idade:")
print('='*50)


while True:
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        print('"Acesso permitido!"')
        break
    elif idade == 12 and idade < 18:
        print('"Acesso necessita autorização de um administrador:')
        break
    else:
        print('Idade menor que 12 anos')
        break
print('\n')
print('Fim do programa!')
print('='*50)