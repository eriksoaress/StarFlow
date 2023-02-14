
import pygame
from classes import*
from variaveis import *
from constantes import*

def inicializa():
    '''Função que inicializa todos os assets e states do jogo'''
    window = pygame.display.set_mode((WIDTH, HEIGHT), vsync=True, flags=pygame.SCALED)
    #Criando o objeto estrela e adicionando no grupo de sprite estrelas
    estrela = Estrela()
    estrelas = pygame.sprite.Group()
    estrelas.add(estrela)
    #Criando o objeto alvo e adicionando no grupo de sprite grupo_alvo
    alvo = Alvo()
    grupo_alvo = pygame.sprite.Group()
    grupo_alvo.add(alvo)
    #Criando o objeto  altera_velocidade e adicionando no grupo de sprite altera_vel_grupo
    altera_vel = Altera_vel()
    altera_vel_grupo= pygame.sprite.Group()
    altera_vel_grupo.add(altera_vel)
    #Criando o objeto  planeta e adicionando no grupo de sprite planeta_grupo
    planeta = Planeta(raio_planeta, posicao_planeta)
    planeta_grupo= pygame.sprite.Group()
    planeta_grupo.add(planeta)





    assets = {
    }

    state = {
        "estrela": estrelas, "alvo":grupo_alvo, "altera_vel" : altera_vel_grupo, "planeta":planeta_grupo
      
    }
    return window, assets, state


def finaliza():
    '''Função utilizada para fechar o pygame'''
    pygame.quit()

def desenha(window: pygame.Surface, assets, state):
    '''Função utilizada para desenhar todos os sprites na tela'''
    state['estrela'].draw(window)
    state['alvo'].draw(window)
    state['altera_vel'].draw(window)
    state['planeta'].draw(window)

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
    window,assets, state = inicializa()
    gameloop(window,assets, state)
    finaliza()