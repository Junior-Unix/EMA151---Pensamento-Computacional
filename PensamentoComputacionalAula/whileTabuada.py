# 2. Construa um programa utilizando o loop while para construir uma tabuada qualquer, o ao
# imprimir a tabuada escolhida o programa deve perguntar se deseja construir outra tabuada,
# caso e escolha seja “S” ou “N”, deve pedir qual a outra chamada a construir ou sair do
# programa.



while True:
    menu = input('Digite o (c)ontinuar ou (s)air: ')
    if menu.lower() == 's':
        break
    multiplicador = int(input(f'Digite o multiplicador: '))
    i = 0
    while i <= 10:
        resultado = multiplicador * i
        print(f'{multiplicador} * {i} = {resultado}')
        i+=1




