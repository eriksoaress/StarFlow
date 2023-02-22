import pygame
import math

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Criar a janela
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Definir a cor de fundo
BACKGROUND_COLOR = (255, 255, 255)

# Definir as dimensões do retângulo
RECT_WIDTH = 100
RECT_HEIGHT = 50

# Definir o ponto de rotação
ROTATION_POINT = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Definir o ângulo inicial de rotação
angle = 0

# Loop principal do jogo
while True:
    # Processar eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Encerrar o jogo se o usuário fechar a janela
            pygame.quit()
            quit()

    # Preencher a tela com a cor de fundo
    screen.fill(BACKGROUND_COLOR)

    # Calcular a posição do retângulo após a rotação
    x = ROTATION_POINT[0] + RECT_WIDTH / 2 * math.cos(math.radians(angle))
    y = ROTATION_POINT[1] + RECT_WIDTH / 2 * math.sin(math.radians(angle))

    # Desenhar o retângulo na posição correta
    rect = pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT)
    pygame.draw.rect(screen, (255, 0, 0), rect)

    # Atualizar o ângulo de rotação
    angle += 1

    # Atualizar a tela
    pygame.display.update()
