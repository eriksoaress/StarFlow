from imports import *
class Game_over(pygame.sprite.Sprite):
    '''Classe para criar a tela de game over'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo da tela de game over
        self.image =pygame.Surface((1280,720))
        self.image.fill((0,0,0))
        self.image.set_alpha(200)

        
        # Definindo o retângulo da imagem
        self.rect = self.image.get_rect()
        self.rect.centerx = 640
        self.rect.centery = 360