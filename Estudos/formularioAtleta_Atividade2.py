# 2. Utilise a instrução if, que permite executar os seguintes passos:
#     a) Entrar com o nome do atleta;
#     b) Entrar com a idade do atleta;
#     c) Entrar com as modalidades:
#         Digitar a opção 1 para Natação;
#         Digitar a opçao 2 para Atletismo;
#         Digitar a opção 3 para Outras.
#
#     As seguintes condições devem ser consideradas:
#     - Se o atleta for maior de 18 anos e nadador indicar a mensagem "Atleta XXX preencher o formulário para participar da seletiva".
#     - Se o atleta for maior de 18 anos e praticar atletismo indicar a mensagem "Atleta XXX seguir para a avaliação com o técnico".
#     - Se o atleta for maior de 18 anos e praticar outra modalidade indicar a mensagem "Atleta XXX para sua modalidade a seletiva será somente em agosto".
#     Demais casos dar a seguinte mensagem "Para participar das seletivas é preciso ter no mínimo 18 anos."
#

while True:
    print('='*50)
    print('Programa para classificar atletas.')
    print('-'*50)

    menu = input("[ENTER] para continuar ou (s)air: ")
    nome = input('Nome: ')
    if nome.lower() == 's':
        print('Saindo do programa.')

    idade = input('Idade: ')
    if idade.lower() == 's':
        print('Saindo do programa.')

    idade = int(idade)
    print('Modalidade: ')
    print('1 - Natação')
    print('2 - Atletismo')
    print('3 - Outras')
    modalidade = input('Escolha uma opção: ')
    if modalidade.lower() == 's':
        print('Saindo do programa.')

    print('='*50)
#    print('\n')
    cadastro = {'Nome': nome.title(), 'Idade': idade, 'Modalidade': modalidade}
    for chave, valor in cadastro.items():
        print('{} : {}'.format (chave, valor))

#    print('\n')
    print('=' * 50)

    if cadastro['Idade'] >= 18 and cadastro['Modalidade'] == '1':
        print('"Atleta {} preencher o formulário para participar da seletiva"'.format(cadastro['Nome']))
    elif cadastro['Idade'] >= 18 and cadastro['Modalidade'] == '2':
        print('"Atleta [{}] seguir para avaliação com o técnico"'.format(cadastro['Nome']))
    elif cadastro['Idade'] >= 18 and cadastro['Modalidade'] == '3':
        print('"Atleta [{}] para sua modalidade [{}] a seletiva será somente em agosto"'.format(cadastro['Nome'], cadastro['Modalidade']))
    else:
        print('"Para participar das seletivas é preciso ter no mínimo 18 anos."')
#    print('='*50)

    print('\n')
    print('='*50)
    break
print('Programa encerrado.')
print('='*50)
