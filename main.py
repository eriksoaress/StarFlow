
import pygame
from classes import*
import variaveis
from constantes import*

def inicializa():
    '''Função que inicializa todos os assets e states do jogo'''

    assets = {
    }

    state = {
      
    }
    return window, assets, state


def finaliza():
    '''Função utilizada para fechar o pygame'''
    pygame.quit()

def desenha(window: pygame.Surface, assets, state):
    '''Função utilizada para desenhar todos os sprites na tela'''
    pygame.display.update()

def atualiza_estado(state):
    '''Função utilizada para atualizar os estados do jogo'''

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            '''caso o jogador tenha pressionado o botão do mouse'''
            return False

    return True

def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)

if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()