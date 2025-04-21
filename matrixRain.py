import random
import time
import os

# Caracteres usados na chuva
chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Tempo de execução
duration = 5  # segundos
end_time = time.time() + duration

while time.time() < end_time:
    # Gera uma linha aleatória de caracteres
    rain = "".join(random.choice(chars) for _ in range(50))

    print(rain)

    # Pequeno atraso para criar o efeito de queda
    time.sleep(0.1)

    # Limpa a tela para simular movimento (funciona melhor no terminal)
    os.system("cls" if os.name == "nt" else "clear")
