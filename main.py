
import pygame
from classes import*
from variaveis import *
from constantes import*
import numpy as np
from pathlib import Path
import random
import time
FPS = 60  # Frames per Second
clock = pygame.time.Clock()


def reset_game(window,assets, state):
    gameloop(window, assets, state)

def gera_planeta(raio, posicao):
    '''Função que gera o planeta'''
    planeta = Planeta(raio, posicao)
    return planeta
def gera_asteroide(raio, posicao):
    '''Função que gera o asteroide'''
    angle = random.random()
    increment = random.random()
    print(angle)
    asteroide = Asteroide(raio, posicao,angle, max(0.3,increment) )
    return asteroide
def inicializa():
    # Inicializa o Pygame
  
    pygame.init()

    vida = Vida(5)
    vidas = pygame.sprite.Group()
    vidas.add(vida)

    game_over = Game_over()
    game_overs = pygame.sprite.Group()
    game_overs.add(game_over)
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
    angle = random.random()
    increment = random.random()
    asteroide = Asteroide(5,posicao_planeta, angle, max(0.3, 0.7*increment))
    asteroides = pygame.sprite.Group()
    asteroides.add(asteroide)

    planetas= pygame.sprite.Group()
    planetas.add(planeta)
    #Criando o objeto poeira e adicionando no grupo de sprite poeiras
    poeira = Poeira(raio_poeira, raio_poeira, posicao_poeira)
    poeiras = pygame.sprite.Group()
    poeiras.add(poeira)

    #Define a fonte de texto com tamanho 40
    font3 = pygame.font.Font(None,40)
    
    # Renderiza o texto "Game Over" na cor vermelha (RED) utilizando a fonte definida anteriormente
    text = font3.render('Game Over', True, RED)
    #Define as posições e dimensões dos retângulos para os botões da tela de game over
    screen_help_rect = pygame.Rect(361, 7, 63, 31)
    principal_menu_rect = pygame.Rect(74, 396, 252, 59)
    play_again_rect = pygame.Rect(74, 321, 252, 59)
    exit_rect = pygame.Rect(74, 471, 252, 59)
    #Define a posição central do retângulo que contém o texto "Game Over"
    text_rect = text.get_rect(center = (20,20))


    # Cria uma instância da classe Tela_inicial e adiciona a tela em um grupo de telas iniciais
    tela_inicial = Tela_inicial()
    telas_iniciais = pygame.sprite.Group()
    telas_iniciais.add(tela_inicial)
    #Cria um grupo que contém a tela de ajuda e adiciona essa tela ao grupo
    all_help_screen = pygame.sprite.Group()
    help_screen = Help()
    all_help_screen.add(help_screen)

    selecionar = pygame.mixer.Sound(path / "som/selecionar.mp3")
   

    


    assets = {"fundo":pygame.transform.scale(pygame.image.load(path / 'imagens/wallpaper_estrelas.jpeg'), (1280,720))
    , "fundo_instrucoes": pygame.transform.scale(pygame.image.load(path / 'imagens/fundo_instrucoes.jpeg'), (1280,720)),
    'fundo_inicio': pygame.transform.scale(pygame.image.load(path / 'imagens/wallpaper_inicio.png'), (1280,720)),"selecionar": selecionar }
    contador = 0

    

    state = {
        "estrela": estrela,"estrelas": estrelas, "alvos":alvos, "alvo":alvo,
        "planetas":planetas,"planeta":[planeta], "em_andamento": False, 
        "velocidade": np.array([0,0]),"atingiu": False, "pontos": 0, "arrastando": False, 
        "tela_inicial": True, "tela_final": False, "tela_jogo": False, "tela_instrucoes": False, "tela_creditos": False,
        'play_again_rect': play_again_rect, 'exit_rect': exit_rect,'principal_menu_rect': principal_menu_rect, 'screen_help_rect': screen_help_rect,
        'font3':font3,'all_help_screen': all_help_screen, "fase": 1, "inicio_fase": True,
        'font3':font3,'all_help_screen': all_help_screen, "record":  str(open(path / 'record.txt', 'r').read()), "poeiras": poeiras,'poeira':poeira,'asteroide': [asteroide],
         'asteroides': asteroides, 'contador': contador, 'vidas': vidas, 'vida': vida, 'num_vidas': 5, "fim_de_jogo":False, 'game_overs':game_overs, 'game_over':game_over,
         'acertou_3_seguidas':0
     
    }
    return window, assets, state


def finaliza():
    '''Função utilizada para fechar o pygame'''
    pygame.quit()

angle = 0
def desenha(window: pygame.Surface, assets, state):

    
    # Define as cores globais para serem utilizadas na tela inicial
    global COR_1
    global COR_2
    global COR_3

    if state['tela_inicial']:
        # Desenha a tela inicial do jogo
        window.blit(assets['fundo_inicio'], (0,0))
        
        # Define as fontes utilizadas na tela inicial
        fonte = pygame.font.SysFont('Arial', 40)
        fonte_pontos = pygame.font.SysFont('Arial', 16)

        # Renderiza os textos da tela inicial
        iniciar_jogo = fonte.render('Iniciar jogo', True, COR_1)
        sair = fonte.render('Sair', True, COR_2)
        instrucoes = fonte.render('Instruções', True, COR_3)
        pontos_record = fonte_pontos.render('Record: {}'.format(state['record']), True, (255, 255, 255))

        # Obtém as posições dos textos
        posicao_iniciar_jogo = iniciar_jogo.get_rect()
        posicao_sair = sair.get_rect()
        posicao_instrucoes = instrucoes.get_rect()
        posicao_record = pontos_record.get_rect()

        # Define as posições dos textos
        posicao_iniciar_jogo.topright = (700, 300)
        posicao_sair.topright = (645, 500)
        posicao_instrucoes.topright = (695, 400)
        posicao_record.topright = (1270, 0)

        # Desenha os textos na tela
        window.blit(iniciar_jogo, posicao_iniciar_jogo)
        window.blit(instrucoes, posicao_instrucoes)
        window.blit(sair, posicao_sair)
        window.blit(pontos_record, posicao_record)

        # Verifica se o mouse está sobre um dos botões e altera a cor do texto
        if posicao_iniciar_jogo.collidepoint(pygame.mouse.get_pos()):
            
          
            
            COR_1 = (255, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                # Inicia o jogo
                assets['selecionar'].play()
                state['tela_inicial'] = False
                state['tela_jogo'] = True
        else:
            COR_1 = (255, 255, 255)

        if posicao_sair.collidepoint(pygame.mouse.get_pos()):
           
            COR_2 = (255, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                assets['selecionar'].play()
                # Finaliza o jogo
                
                finaliza()
        else:
            COR_2 = (255, 255, 255)
        
        if posicao_instrucoes.collidepoint(pygame.mouse.get_pos()):
            
            COR_3 = (255, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                assets['selecionar'].play()
                # Abre a tela de instruções
                state['tela_inicial'] = False
                state['tela_instrucoes'] = True
        else:
            COR_3 = (255, 255, 255)

        

        
    if state['tela_instrucoes']:
        
        # Define a fonte e tamanho da fonte para o texto 'Voltar'
        fonte = pygame.font.SysFont('Arial', 40)

        # Renderiza o texto 'Voltar' com a fonte definida
        voltar = fonte.render('Voltar', True, (0,0,0))

        # Obtém as dimensões da imagem de 'Voltar' renderizada
        posicao_voltar = voltar.get_rect()

        # Define a posição da imagem de 'Voltar' no canto superior direito da tela
        posicao_voltar.topright = (700, 600)

        # Desenha a imagem de fundo da tela de instruções na janela
        window.blit(assets['fundo_instrucoes'], (0,0))

        # Desenha a imagem de 'Voltar' na janela na posição definida
        window.blit(voltar, posicao_voltar)

        # Verifica se o mouse está sobre a imagem de 'Voltar'
        if posicao_voltar.collidepoint(pygame.mouse.get_pos()):
            # Verifica se o botão esquerdo do mouse está pressionado
            if pygame.mouse.get_pressed()[0]:
                # Define as variáveis de estado para retornar à tela inicial
                state['tela_inicial'] = True
                state['tela_instrucoes'] = False

        
        
    if state['tela_jogo']:


        clock.tick(FPS)
        '''Função utilizada para desenhar todos os sprites na tela'''
        # Define a cor de fundo da tela e desenha o fundo do jogo
        window.fill((0,0,0))
        window.blit(assets['fundo'], (0,0))

        # Desenha o score do jogador
        fonte_pontos = pygame.font.SysFont('Arial', 16)
        pontos_texto = fonte_pontos.render('Score: {}'.format(state['pontos']), True, (255, 255, 255))
        posicao_texto = pontos_texto.get_rect()
        posicao_texto.topright = (1270, 0)
        window.blit(pontos_texto, posicao_texto)

        # Desenha uma linha caso o jogador esteja arrastando uma estrela
        if state['arrastando'] == True:
            pygame.draw.line(window, (255, 255, 255), posicao_inicial_estrela, pygame.mouse.get_pos(), 1)


        # Desenha todos os sprites na tela
        state['estrelas'].draw(window)
        state['alvos'].draw(window)
        state['planetas'].draw(window)
        state['poeiras'].draw(window)
        state['asteroides'].draw(window)
        state['vidas'].draw(window)

        # Desenha uma linha colorida quando o jogador arrasta uma estrela
       
        
        if state['arrastando'] == True:
            #Desenha uma linha de cor que varia entre verde e vermelho com base na distância entre a posição inicial da estrela arrastada e a posição atual do mouse
            #A cor da linha é determinada pelo valor mínimo entre a distância e 255
            color_line = min(((pygame.mouse.get_pos()[0]  - posicao_inicial_estrela[0])**2  + (pygame.mouse.get_pos()[1]  - posicao_inicial_estrela[1] )**2)**0.5, 255)

            pygame.draw.line(window, (0 + color_line, 255 - color_line , 0), posicao_inicial_estrela, pygame.mouse.get_pos(), 2)
            pygame.draw.line(window, (0 + color_line, 255 - color_line , 0), posicao_inicial_estrela + np.array([0,-15]), pygame.mouse.get_pos() + np.array([0,-2]), 2)
        
    #Gera novos planetas se a pontuação dividida pela fase atual for maior do que 5 e o número de planetas for menor do que 3
    if state['pontos']/state['fase'] > 5 and len(state['planeta']) < 3 :
        #Gera um novo planeta com tamanho entre 20 e 50 pixels e posição aleatória na tela
        planeta = gera_planeta(random.randint(20, 50), np.array([random.randint(400, 1100), random.randint(100, 650)]))
        asteroide = gera_asteroide(random.randint(5, 10), np.array([planeta.rect.centerx, planeta.rect.centery]))
        state['asteroide'].append(asteroide)
        state['asteroides'].add(asteroide)
        #Adiciona o planeta na lista de planetas do jogo
        state['planeta'].append(planeta)
        #Adiciona o planeta ao grupo de sprites de planetas
        state['planetas'].add(planeta)
        #Incrementa a fase atual do jogo
        state['fase'] += 1

    if state['fim_de_jogo']:
        
        # Desenha a tela inicial do jogo
        window.blit(assets['fundo_inicio'], (0,0))
        
        # Define as fontes utilizadas na tela inicial
        fonte_game_over = pygame.font.SysFont('Arial', 90)
        fonte = pygame.font.SysFont('Arial', 40)
        fonte_pontos = pygame.font.SysFont('Arial', 95)

        # Renderiza os textos da tela inicial
        game_over = fonte.render('Game over', True,(255, 255, 255))
        jogar_novamente = fonte.render('Jogar novamente', True, COR_1)
        menu_principal = fonte.render('Menu Principal', True, COR_2)
        sair = fonte.render('Sair', True, COR_3)

        pontos_record = fonte_pontos.render('Record: {}'.format(state['record']), True, (255, 255, 255))

        # Obtém as posições dos textos e retangulos
        posicao_game_over = game_over.get_rect(center = (640, 50))
        posicao_jogar_novamente = jogar_novamente.get_rect(center = (640, 350))
        posicao_sair = sair.get_rect( center = (640, 450))
        posicao_record = pontos_record.get_rect(center = (640, 200))


        # Desenha os textos na tela
        window.blit(game_over, posicao_game_over)
        window.blit(sair, posicao_sair)
        window.blit(pontos_record, posicao_record)
        window.blit(jogar_novamente, posicao_jogar_novamente)
       
        # Verifica se o mouse está sobre um dos botões e altera a cor do texto
        if posicao_jogar_novamente.collidepoint(pygame.mouse.get_pos()):
            
          
            
            COR_1 = (255, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                # Inicia o jogo
                assets['selecionar'].play()
                window,assets, state = inicializa()
                reset_game(window, assets, state)
                finaliza()
        else:
            COR_1 = (255, 255, 255)

        
        
        if posicao_sair.collidepoint(pygame.mouse.get_pos()):
            
            COR_3 = (255, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                assets['selecionar'].play()
                # Abre a tela de instruções
                state['tela_jogo'] = False
                state['fim_de_jogo'] = False
                finaliza()
        else:
            COR_3 = (255, 255, 255)


        # Define a fonte e tamanho da fonte para o texto 'Voltar'
        fonte = pygame.font.SysFont('Arial', 40)
    if state['acertou_3_seguidas'] == 3:
        if state['num_vidas']< 5:
            state['vida'].update(state['num_vidas'] + 1)
            state['num_vidas'] += 1
            state['acertou_3_seguidas'] = 0

    # Atualiza a tela
    pygame.display.update()

def atualiza_estado(state):
    global velocidade
    global angle
    '''Função utilizada para atualizar os estados do jogo'''
  
    # Verifica eventos do Pygame
    for ev in pygame.event.get():
        # Verifica se o usuário clicou no botão "X" para fechar a janela
        if ev.type == pygame.QUIT:
            # Se o estado atual tiver mais pontos do que o recorde, atualiza o recorde
            if state['pontos'] > int(state['record']):
                # Abre o arquivo em modo de escrita e escreve a nova pontuação
                with open(path / 'record.txt', 'w') as file:
                    file.write(str(state['pontos']))
                    # Atualiza o recorde com a nova pontuação
                    state['record'] = state['pontos']
            # Retorna "False" para indicar que o jogo deve ser encerrado
            return False
        
        # Verifica se o usuário clicou com o botão esquerdo do mouse
        posicao_mouse = np.array(pygame.mouse.get_pos())
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                # Verifica se o jogo está em andamento
                if state['em_andamento'] == False:
                    # Verifica se o mouse está sobre a estrela
                    if state['estrela'].rect.collidepoint(ev.pos):
                        # Move a estrela para a posição atual do mouse e marca que está sendo arrastada
                        state['estrela'].rect.center = pygame.mouse.get_pos()
                        state['arrastando'] = True
        # Verifica se o usuário soltou o botão esquerdo do mouse
        elif ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 1:
                # Verifica se a estrela está sendo arrastada
                if state['arrastando'] == True:
                    # Calcula a velocidade com que a estrela deve ser lançada
                    velocidade =  posicao_inicial_estrela - posicao_mouse
                    modulo_velocidade= (velocidade[0]**2 + velocidade[1]**2)**0.5
                    unitario = velocidade/modulo_velocidade
                    if modulo_velocidade> 100:
                        velocidade = unitario*100
                    modulo_velocidade= (velocidade[0]**2 + velocidade[1]**2)**0.5
                    # Armazena a velocidade no estado atual do jogo e atualiza a posição da estrela
                    state['velocidade'] = velocidade
                    state['estrela'].update(state['velocidade'], state['atingiu'])
                    # Marca que o jogo está em andamento
                    state['em_andamento'] = True
                # Marca que a estrela não está mais sendo arrastada
                state['arrastando'] = False
        # Se o usuário está arrastando a estrela, atualiza a posição dela para a posição atual do mouse
        elif state['arrastando'] == True:
            state['estrela'].rect.center = pygame.mouse.get_pos()
    
                   
    if state['contador']%5 == 0 :    
        state['poeira'].update()  
    state['contador'] += 1        
              
    # Verifica se houve colisão entre a estrela e os alvos
    if pygame.sprite.spritecollide(state['estrela'], state['alvos'], False):
        state['acertou_3_seguidas'] += 1
        # Adiciona um ponto
        state['pontos'] += 1
        # Atualiza a posição do alvo
        state['alvo'].update()
        # Atualiza a posição da poeira
        #state['poeira'].update()
        # Zera a velocidade
        state['velocidade'] *= 0
        # Atualiza a posição da estrela
        state['estrela'].update(state['velocidade'], True)
        # Define que o jogo não está mais em andamento
        state['em_andamento'] = False

    # Verifica se a estrela passou da tela
    passou_da_tela = state['estrela'].update(state['velocidade'], False)
  
    if passou_da_tela:
        
        state['acertou_3_seguidas'] = 0

        if state['num_vidas'] > 1:
            state['num_vidas'] -= 1
        else:
            state['tela_jogo'] = False
            state['fim_de_jogo'] = True
        state['vida'].update(state['num_vidas'])
        # Zera a velocidade
        state['velocidade'] *= 0
        # Define que o jogo não está mais em andamento
        state['em_andamento'] = False

        # Verifica se a pontuação atual é maior que a pontuação recorde
        if state['pontos'] > int(state['record']):
            # Abre o arquivo de recorde em modo de escrita
            with open(path / 'record.txt', 'w') as file:
                # Escreve a nova pontuação no arquivo
                file.write(str(state['pontos']))
            # Atualiza o recorde com a nova pontuação
            state['record'] = state['pontos']

        # Diminui um ponto da pontuação
        if state['pontos'] > 0:
            state['pontos'] -= 1

    # Verifica se o jogo está em andamento
    if state['em_andamento']:
        # Atualiza a posição dos planetas
        for i in range(state['fase']):
            state['planeta'][i].update(state)

    # Atualiza a posição do asteroide
    for i in range(state['fase']):
        state['asteroide'][i].update(np.array([state['planeta'][i].rect.centerx, state['planeta'][i].rect.centery ]))
    

   

    # Retorna "True" para indicar que o jogo continua em andamento
    
    return True

def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)
      

if __name__ == '__main__':
    window,assets, state = inicializa()
    gameloop(window,assets, state)
    finaliza()
