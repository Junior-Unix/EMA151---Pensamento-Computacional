import time
import sys

# Simulação de condição
condicao = True  # Altere para False para testar o outro caminho

if condicao:
    print("Processando...")
    for i in range(3):  # Loop para 3 segundos
        sys.stdout.write("..")
        sys.stdout.flush()
        time.sleep(1)
    print("\nAção realizada no bloco 'if'.")
else:
    print("Carregando alternativa...")
    for i in range(3):
        sys.stdout.write("..")
        sys.stdout.flush()
        time.sleep(1)
    print("\nAção realizada no bloco 'else'.")
