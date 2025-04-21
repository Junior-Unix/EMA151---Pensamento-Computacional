import time
import sys

# Caracteres da hélice
helice = ["|", "/", "-", "\\"]

# Tempo total da animação
duration = 4  # segundos
end_time = time.time() + duration

while time.time() < end_time:
    for simbolo in helice:
        sys.stdout.write(f"\r{simbolo}")  # Escreve no mesmo espaço da linha
        sys.stdout.flush()  # Atualiza o texto no terminal
        time.sleep(0.2)  # Pequeno atraso para simular rotação
