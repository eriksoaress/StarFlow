
import pygame
from classes import*
from variaveis import *
from constantes import*
import numpy as np

def inicializa():
    '''Função que inicializa todos os assets e states do jogo'''
    window = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED)
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

    #Criando o objeto  mira e adicionando no grupo de sprite mira_grupo

    mira = Mira1()
    mira_grupo= pygame.sprite.Group()
    mira_grupo.add(mira)
    mira2 = Mira2()
    mira_grupo2= pygame.sprite.Group()
    mira_grupo2.add(mira2)






    assets = {
    }

    state = {
        "estrela": estrelas,"estrela_obj": estrela, "alvo":grupo_alvo, "altera_vel" : altera_vel_grupo,
         "planeta":planeta_grupo, "em_andamento": False, "velocidade": np.array([0,0]), 'mira':mira_grupo, 'mira_obj': mira,
         'mira2':mira_grupo2, 'mira_obj2': mira2
      
    }
    return window, assets, state


def finaliza():
    '''Função utilizada para fechar o pygame'''
    pygame.quit()

def desenha(window: pygame.Surface, assets, state):
    '''Função utilizada para desenhar todos os sprites na tela'''
    window.fill((0,0,0))
    state['estrela'].draw(window)
    state['alvo'].draw(window)
    state['altera_vel'].draw(window)
    state['planeta'].draw(window)
    state['mira'].draw(window)
    state['mira2'].draw(window)


    pygame.display.update()

def atualiza_estado(state):
    '''Função utilizada para atualizar os estados do jogo'''
    direita = 1
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            
            '''caso o jogador tenha pressionado o botão seta pra cima'''
            direita = 2
            state['mira_obj'].update(direita)
            state['mira_obj2'].update(direita)
        if keys[pygame.K_RIGHT]:
            '''caso o jogador tenha pressionado o botão seta pra cima'''
            direita = 3
            state['mira_obj'].update(direita)
            state['mira_obj2'].update(direita)
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if state['em_andamento'] == False:
                    if ev.pos[0] >= 440 and ev.pos[0] <=840 and ev.pos[1] >= 670:
                        x = pygame.mouse.get_pos()[0] - 440
                        state['velocidade'][0] = x/100
                        state['em_andamento'] = True
    state['estrela_obj'].update(state['velocidade'])

 




            
    
    
        

    return True

def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)
      

if __name__ == '__main__':
    window,assets, state = inicializa()
    gameloop(window,assets, state)
    finaliza()