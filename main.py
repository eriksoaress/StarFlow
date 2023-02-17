
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
    alvos = pygame.sprite.Group()
    alvos.add(alvo)
    #Criando o objeto  altera_velocidade e adicionando no grupo de sprite altera_vel_grupo
    altera_velocidade = Altera_vel()
    altera_velocidades= pygame.sprite.Group()
    altera_velocidades.add(altera_velocidade)
    #Criando o objeto  planeta e adicionando no grupo de sprite planeta_grupo
    planeta = Planeta(raio_planeta, posicao_planeta, False)
    planetas= pygame.sprite.Group()
    planetas.add(planeta)


    velocidade = np.array([0,0])



    assets = {"fundo":pygame.transform.scale(pygame.image.load('''/home/fernando/Faculdade/3 semestre/Algelin. Teo. Info/aps0/jogo/StarFlow/wallpaper_estrelas.jpeg'''), (1280,720))
    }

    state = {
        "estrela": estrela,"estrelas": estrelas, "alvos":alvos, "alvo":alvo, "altera_velocidades" : altera_velocidades, 
        "planetas":planetas,"planeta":planeta, "em_andamento": False, "velocidade": np.array([0,0]), "atingiu": False, 
        "pontos": 0
      
    }
    return window, assets, state


def finaliza():
    '''Função utilizada para fechar o pygame'''
    pygame.quit()

def desenha(window: pygame.Surface, assets, state):
    '''Função utilizada para desenhar todos os sprites na tela'''
    window.fill((0,0,0))
    window.blit(assets['fundo'], (0,0))
    state['estrelas'].draw(window)
    state['alvos'].draw(window)
    state['altera_velocidades'].draw(window)
    state['planetas'].draw(window)



    pygame.display.update()

def atualiza_estado(state):
    '''Função utilizada para atualizar os estados do jogo'''
  
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
      
        posicao_mouse = np.array(pygame.mouse.get_pos())
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if state['em_andamento'] == False:
                    
                    velocidade =  posicao_inicial_estrela - posicao_mouse 
                    state['velocidade'] = velocidade
                    state['estrela'].update(state['velocidade'], state['atingiu'])
                    state['em_andamento'] = True
    
                   
                    
                        
    if state['em_andamento']:
        state['planeta'].update(state['estrela'],state['velocidade'])            
    if pygame.sprite.spritecollide(state['estrela'], state['alvos'], False) :
        state['pontos']+= 1
        state['alvo'].update()
        state['estrela'].update(state['velocidade'],True)
        state['velocidade'] *= 0
        state['em_andamento'] = False
    
    passou_da_tela = state['estrela'].update(state['velocidade'], False)
    # state['planeta'].update(state['velocidade'],np.array([state['estrela_obj'].rect.centerx, state['estrela_obj'].rect.centery]), state['estrela_obj'])
    if passou_da_tela:
        state['velocidade'] *= 0
        state['em_andamento'] = False
 




            
    
    
        

    return True

def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)
      

if __name__ == '__main__':
    window,assets, state = inicializa()
    gameloop(window,assets, state)
    finaliza()