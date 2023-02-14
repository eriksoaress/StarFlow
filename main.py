import numpy as np
import pygame
import math
import random

pygame.init()

# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

COR_PERSONAGEM = (30, 200, 20)


# Inicializar posicoes
s0 = np.array([615, 660])
v0 = np.array([0, 0])
rect_power = np.array([20, 80])

v = v0
s = s0

# Personagem
personagem = pygame.Surface((50, 50))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem



rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False


    # Controlar frame rate
    clock.tick(FPS)

    # Processar posicoes

    # Desenhar fundo
    screen.fill((0,0,0))

    # Desenhar personagem
    rect = pygame.Rect(s, (50,50))  # First tuple is position, second is size.
    screen.blit(personagem, rect)
   


    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()