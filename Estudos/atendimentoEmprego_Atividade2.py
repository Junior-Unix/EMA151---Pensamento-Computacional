# 3.  Numa empresa de empregos ao chegar na receção o interessado em buscar uma oportunidade
#     de trabalho responde a seguintes questões.
#         a) Nome do candidato;
#         b) Ano de nascimento;
#         c) Formação que tem as opções:
#             - cursando o ensino médio (0);
#             - ensino médio (1);
#             - cursando ensino superior (2);
#             - curso superior (3).
#         d) Tempo de experiência na área de formação (em anos);
#         e) Fluência em inglês.
#
#     Escrever um script que leia os dados de entrada pelo teclado, classifique e encaminhe o interessado para ser atendido, conforme segue:
#
#         - Maior de 30 anos com opção 3, mais de 8 anos de experiência e fluência em inglês - "Siga para atendimento até o 4º Andar e aguarde na sala 4A que será chamado pelo nome.";
#         - Maior de 30 anos com a opção 3, menos de 8 anos de esperiência e com fluência em inglês - "Siga para atendimento até o 4º Andar e aguerde na sala 4B que será chamado pelo nome.";
#         - Maior de 25 anos com opção 3, enos de 2 anos de esperiência e fluência em inglês - "Siga para atendimento até o 3º Andar e aguarde na sala 3A qe será chamado pelo nome.";
#         - Maior de 25 anos, opção 3, sem fluência em inglês - "Siga para atendimento até o 2º andar e aguarde na sala 2B que será chamado pelo nome.";
#         - Demais casos - "Siga para atendimento até o 1º Andar e aguarde ser chamado pelo nome.".

print('='*50)
print('PROGRAMA DE CLASSIFICAÇÃO DE CANDIDATOS A EMPREGO')
print('='*50)

nome = str(input('digite seu nome: '))
anoNascimento = int(input('Digite seu ano de nascimento: '))
formacao = int(input('Digite sua formação \n\t 0 - Cursando Ensino Médio \n\t 1 - Ensino Médio \n\t 2 - Cursando Superior \n\t 3 - Curso Superior \nOpção: '))
tempoExperiencia = int(input('Digite seu tempo de experiência na área de formação (em anos): '))
fluenciaIngles = str(input('Você tem fluência em inglês? (s/n): '))
if fluenciaIngles.lower() == 's':
    fluenciaIngles = 's'
elif fluenciaIngles.lower() == 'n':
    fluenciaIngles = 'n'
idade = int(2025 - anoNascimento)

print('='*50)
if idade > 30 and formacao == 3 and tempoExperiencia > 8 and fluenciaIngles == 's':
    print('Siga para atendimento até o 4º Andar e aguarde na sala 4A que será chamado pelo nome.')
elif idade > 30 and formacao == 3 and tempoExperiencia < 8 and fluenciaIngles == 's':
    print('Siga para atendimento até o 4º Andar e aguarde na sala 4B que será chamado pelo nome.')
elif idade > 25 and formacao == 3 and tempoExperiencia > 2 and fluenciaIngles == 's':
    print('Siga para atendimento até o 3º Andar e aguarde na sala 3A que será chamado pelo nome.')
elif idade > 25 and formacao == 3 and fluenciaIngles == 'n':
    print('Siga para atendimento até o 2º andar e aguarde na sala 2B que será chamado pelo nome.')
else:
    print('Siga para atendimento até o 1º Andar e aguarde ser chamado pelo nome.')
print('='*50)
print('FIM DO PROGRAMA')
