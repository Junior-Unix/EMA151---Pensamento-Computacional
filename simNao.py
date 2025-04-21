#  De quantas formas podemos responder a 12 perguntas de um questionário, cujas
# respostas para cada pergunta são: sim ou não?
from itertools import product

# Lista de "Sim" (S) ou "Não" (N)
respostas = ["S", "N"]

# Gerar combinações
combinacoes = product(respostas, repeat=12)

# Abrir arquivo para escrita
with open("resultados.txt", "w") as arquivo:
    # Exibir todas as possibilidades com cores e salvar no arquivo
    for sequencia in combinacoes:
        resultado = ''.join([f"\033[92m{resposta}\033[0m" if resposta == "S" else f"\033[91m{resposta}\033[0m" for resposta in sequencia])
        print(resultado)
        arquivo.write(''.join(sequencia) + "\n")