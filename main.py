
import pygame
from classes import*
from variaveis import *
from constantes import*
import numpy as np
from pathlib import Path

FPS = 60  # Frames per Second
clock = pygame.time.Clock()

def gera_planeta(raio, posicao):
    '''Função que gera o planeta'''
    planeta = Planeta(raio, posicao)
    return planeta

def inicializa():
    # Inicializa o Pygame
  
    pygame.init()
   
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

    planeta = Planeta(raio_planeta, posicao_planeta)

    planetas= pygame.sprite.Group()
    planetas.add(planeta)
    #Criando o objeto poeira e adicionando no grupo de sprite poeiras
    poeira = Poeira(raio_poeira, raio_poeira, posicao_poeira)
    poeiras = pygame.sprite.Group()
    poeiras.add(poeira)

    font3 = pygame.font.Font(None,40)
    

    text = font3.render('Game Over', True, RED)
    screen_help_rect = pygame.Rect(361, 7, 63, 31)
    principal_menu_rect = pygame.Rect(74, 396, 252, 59)
    play_again_rect = pygame.Rect(74, 321, 252, 59)
    exit_rect = pygame.Rect(74, 471, 252, 59)
    text_rect = text.get_rect(center = (20,20))



    tela_inicial = Tela_inicial()
    telas_iniciais = pygame.sprite.Group()
    telas_iniciais.add(tela_inicial)

    all_help_screen = pygame.sprite.Group()
    help_screen = Help()
    all_help_screen.add(help_screen)

    


    assets = {"fundo":pygame.transform.scale(pygame.image.load(path / 'imagens/wallpaper_estrelas.jpeg'), (1280,720))
    , "fundo_instrucoes": pygame.transform.scale(pygame.image.load(path / 'imagens/fundo_instrucoes.jpeg'), (1280,720)),
    'fundo_inicio': pygame.transform.scale(pygame.image.load(path / 'imagens/wallpaper_inicio.png'), (1280,720)), }

    

    state = {
        "estrela": estrela,"estrelas": estrelas, "alvos":alvos, "alvo":alvo,
        "planetas":planetas,"planeta":[planeta], "em_andamento": False, 
        "velocidade": np.array([0,0]),"atingiu": False, "pontos": 0, "arrastando": False, 
        "tela_inicial": True, "tela_final": False, "tela_jogo": False, "tela_instrucoes": False, "tela_creditos": False,
        'play_again_rect': play_again_rect, 'exit_rect': exit_rect,'principal_menu_rect': principal_menu_rect, 'screen_help_rect': screen_help_rect,
        'font3':font3,'all_help_screen': all_help_screen, "fase": 1, "inicio_fase": True,
        'font3':font3,'all_help_screen': all_help_screen, "record":  str(open(path / 'record.txt', 'r').read()), "poeiras": poeiras
     
    }
    return window, assets, state


def finaliza():
    '''Função utilizada para fechar o pygame'''
    pygame.quit()

def desenha(window: pygame.Surface, assets, state):

    global COR_1
    global COR_2
    global COR_3


    if state['tela_inicial']:
        '''Desenha a tela inicial do jogo'''
        window.blit(assets['fundo_inicio'], (0,0))
        fonte = pygame.font.SysFont('Arial', 40)
        fonte_pontos = pygame.font.SysFont('Arial', 16)
        iniciar_jogo = fonte.render('Iniciar jogo', True, COR_1)
        sair = fonte.render('Sair', True, COR_2)
        instrucoes = fonte.render('Instruções', True, COR_3)
        pontos_record = fonte_pontos.render('Record: {}'.format(state['record']), True, (255, 255, 255))

        posicao_iniciar_jogo = iniciar_jogo.get_rect()
        posicao_sair = sair.get_rect()
        posicao_instrucoes = instrucoes.get_rect()
        posicao_record = pontos_record.get_rect()


        posicao_iniciar_jogo.topright = (700, 300)
        posicao_sair.topright = (645, 500)
        posicao_instrucoes.topright = (695, 400)
        posicao_record.topright = (1270, 0)

        window.blit(iniciar_jogo, posicao_iniciar_jogo)
        window.blit(instrucoes, posicao_instrucoes)
        window.blit(sair, posicao_sair)
        window.blit(pontos_record, posicao_record)

        if posicao_iniciar_jogo.collidepoint(pygame.mouse.get_pos()):
            COR_1 = (255, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                state['tela_inicial'] = False
                state['tela_jogo'] = True
        else:
            COR_1 = (255, 255, 255)

        if posicao_sair.collidepoint(pygame.mouse.get_pos()):
            COR_2 = (255, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                finaliza()
        else:
            COR_2 = (255, 255, 255)
        
        if posicao_instrucoes.collidepoint(pygame.mouse.get_pos()):
            COR_3 = (255, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                state['tela_inicial'] = False
                state['tela_instrucoes'] = True
        else:
            COR_3 = (255, 255, 255)
        

        
    if state['tela_instrucoes']:
        '''Desenha a tela de instruções do jogo'''
        fonte = pygame.font.SysFont('Arial', 40)
        voltar = fonte.render('Voltar', True, (0,0,0))
        posicao_voltar = voltar.get_rect()
        posicao_voltar.topright = (700, 600)
        window.blit(assets['fundo_instrucoes'], (0,0))
        window.blit(voltar, posicao_voltar)
        
        
        
        if posicao_voltar.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                state['tela_inicial'] = True
                state['tela_instrucoes'] = False
  
        
        
    if state['tela_jogo']:


        clock.tick(FPS)
        '''Função utilizada para desenhar todos os sprites na tela'''
        window.fill((0,0,0))
        window.blit(assets['fundo'], (0,0))
        fonte_pontos = pygame.font.SysFont('Arial', 16)
        pontos_texto = fonte_pontos.render('Score: {}'.format(state['pontos']), True, (255, 255, 255))
        posicao_texto = pontos_texto.get_rect()
        posicao_texto.topright = (1270, 0)
        window.blit(pontos_texto, posicao_texto)
        if state['arrastando'] == True:
            pygame.draw.circle(window, (255,255,255), posicao_inicial_estrela, 3)
        if state['arrastando'] == True:
            pygame.draw.line(window, (255, 255, 255), posicao_inicial_estrela, pygame.mouse.get_pos(), 1)
        state['estrelas'].draw(window)
        
        state['alvos'].draw(window)
        state['planetas'].draw(window)
        state['poeiras'].draw(window)
   
        if state['arrastando'] == True:
            color_line = min(((pygame.mouse.get_pos()[0]  - posicao_inicial_estrela[0])**2  + (pygame.mouse.get_pos()[1]  - posicao_inicial_estrela[1] )**2)**0.5, 255)

            pygame.draw.line(window, (0 + color_line, 255 - color_line , 0), posicao_inicial_estrela, pygame.mouse.get_pos(), 2)
        

    if state['pontos']/state['fase'] > 5 :
        planeta = gera_planeta(random.randint(20, 50), np.array([random.randint(400, 1100), random.randint(100, 650)]))
        state['planeta'].append(planeta)
        state['planetas'].add(planeta)
        state['fase'] += 1



    pygame.display.update()

def atualiza_estado(state):
    global velocidade
    '''Função utilizada para atualizar os estados do jogo'''
  
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            if state['pontos'] > int(state['record']):
            # Abre o arquivo em modo de escrita e escreve a nova pontuação
                with open(path / 'record.txt', 'w') as file:
                    file.write(str(state['pontos']))
                # Atualiza o recorde com a nova pontuação
                    state['record'] = state['pontos']
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
                    modulo_velocidade= (velocidade[0]**2 + velocidade[1]**2)**0.5
                    unitario = velocidade/modulo_velocidade
                    if modulo_velocidade> 100:
                        velocidade = unitario*100
                    modulo_velocidade= (velocidade[0]**2 + velocidade[1]**2)**0.5
                    state['velocidade'] = velocidade
                    state['estrela'].update(state['velocidade'], state['atingiu'])
                    state['em_andamento'] = True
                state['arrastando'] = False
        elif state['arrastando'] == True:
            state['estrela'].rect.center = pygame.mouse.get_pos()
    
                   
                    
                        
              
    if pygame.sprite.spritecollide(state['estrela'], state['alvos'], False) :
        state['pontos']+= 1
        state['alvo'].update()
        state['velocidade'] *= 0
        state['estrela'].update(state['velocidade'],True)
        state['em_andamento'] = False
    
    passou_da_tela = state['estrela'].update(state['velocidade'], False)

    if state['em_andamento']:
            for i in range(state['fase']):
                state['planeta'][i].update(state)
       



    # state['planeta'].update(state['velocidade'],np.array([state['estrela_obj'].rect.centerx, state['estrela_obj'].rect.centery]), state['estrela_obj'])
    if passou_da_tela:
        state['velocidade'] *= 0
        state['em_andamento'] = False

        if state['pontos'] > int(state['record']):
            # Abre o arquivo em modo de escrita e escreve a nova pontuação
            with open(path / 'record.txt', 'w') as file:
                file.write(str(state['pontos']))
            # Atualiza o recorde com a nova pontuação
                state['record'] = state['pontos']
        state['pontos'] = 0
   



            
    
    
        

    return True

def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)
      

if __name__ == '__main__':
    window,assets, state = inicializa()
    gameloop(window,assets, state)
    finaliza()