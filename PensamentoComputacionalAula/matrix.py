import pygame
import random

# Inicializar pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Chuva de Letras - Estilo Matrix")

# Cores e fonte
VERDE_MATRIX = (0, 255, 0)
PRETO = (0, 0, 0)
FONT_SIZE = 25
fonte = pygame.font.Font(pygame.font.match_font('monospace'), FONT_SIZE)

# Criar colunas de letras
colunas = [random.randint(0, LARGURA) for _ in range(60)]
posicoes = [random.randint(-ALTURA, 0) for _ in range(60)]
velocidades = [random.randint(5, 15) for _ in range(60)]
textos = [random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(60)]

# Criar rastro das letras
rastros = {coluna: [] for coluna in colunas}

# Loop principal
rodando = True
while rodando:
    tela.fill(PRETO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    for i in range(len(colunas)):
        letra_surface = fonte.render(textos[i], True, VERDE_MATRIX)
        tela.blit(letra_surface, (colunas[i], posicoes[i]))

        # Criar rastro
        rastros[colunas[i]].append((posicoes[i], textos[i]))

        # Limitar tamanho do rastro
        if len(rastros[colunas[i]]) > 10:
            rastros[colunas[i]].pop(0)

        # Renderizar rastro com intensidade reduzida
        for j, (pos_y, letra) in enumerate(rastros[colunas[i]]):
            cor_fade = (0, 255 - j * 25, 0)
            letra_surface = fonte.render(letra, True, cor_fade)
            tela.blit(letra_surface, (colunas[i], pos_y))

        # Atualizar posição
        posicoes[i] += velocidades[i]

        # Reiniciar letras no topo quando alcançam o final da tela
        if posicoes[i] > ALTURA:
            posicoes[i] = random.randint(-FONT_SIZE, 0)
            textos[i] = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
            velocidades[i] = random.randint(5, 15)
            rastros[colunas[i]] = []

    pygame.display.flip()
    pygame.time.delay(30)  # Ajuste para maior velocidade

pygame.quit()
