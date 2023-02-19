
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
    #Criando o objeto  planeta e adicionando no grupo de sprite planeta_grupo
    planeta = Planeta(raio_planeta, posicao_planeta, False)
    planetas= pygame.sprite.Group()
    planetas.add(planeta)



    assets = {"fundo":pygame.transform.scale(pygame.image.load('''wallpaper_estrelas.jpeg'''), (1280,720))
    }

    state = {
        "estrela": estrela,"estrelas": estrelas, "alvos":alvos, "alvo":alvo,
        "planetas":planetas,"planeta":planeta, "em_andamento": False, 
        "velocidade": np.array([0,0]),"atingiu": False, "pontos": 0, "arrastando": False
      
    }
    return window, assets, state


def finaliza():
    '''Função utilizada para fechar o pygame'''
    pygame.quit()

def desenha(window: pygame.Surface, assets, state):
    '''Função utilizada para desenhar todos os sprites na tela'''
    window.fill((0,0,0))
    window.blit(assets['fundo'], (0,0))
    pygame.font.init()
    fonte = pygame.font.SysFont('Arial', 16)
    pontos_texto = fonte.render('Score: {}'.format(state['pontos']), True, (255, 255, 255))
    posicao_texto = pontos_texto.get_rect()
    posicao_texto.topright = (1270, 0)
    window.blit(pontos_texto, posicao_texto)
    if state['arrastando'] == True:
        pygame.draw.circle(window, (255,255,255), posicao_inicial_estrela, 3)
    state['estrelas'].draw(window)
    state['alvos'].draw(window)
    state['planetas'].draw(window)
    if state['arrastando'] == True:
        pygame.draw.line(window, (255, 255, 255), posicao_inicial_estrela, pygame.mouse.get_pos(), 1)




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
                    if state['estrela'].rect.collidepoint(ev.pos):
                        state['estrela'].rect.center = pygame.mouse.get_pos()
                        state['arrastando'] = True
        elif ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 1:
                if state['arrastando'] == True:
                    velocidade =  posicao_inicial_estrela - posicao_mouse 
                    state['velocidade'] = velocidade
                    state['estrela'].update(state['velocidade'], state['atingiu'])
                    state['em_andamento'] = True
                state['arrastando'] = False
        elif state['arrastando'] == True:
            state['estrela'].rect.center = pygame.mouse.get_pos()
    
                   
                    
                        
    if state['em_andamento']:
        state['planeta'].update(state['estrela'],state['velocidade'])            
    if pygame.sprite.spritecollide(state['estrela'], state['alvos'], False) :
        state['pontos']+= 1
        state['alvo'].update()
        state['velocidade'] *= 0
        state['estrela'].update(state['velocidade'],True)
        state['em_andamento'] = False
    
    passou_da_tela = state['estrela'].update(state['velocidade'], False)
    # state['planeta'].update(state['velocidade'],np.array([state['estrela_obj'].rect.centerx, state['estrela_obj'].rect.centery]), state['estrela_obj'])
    if passou_da_tela:
        state['pontos'] = 0
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