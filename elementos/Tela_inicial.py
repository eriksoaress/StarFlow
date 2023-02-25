from imports import *
            
class Tela_inicial(pygame.sprite.Sprite):
    '''Classe para criar a tela inicial'''

    def __init__(self):
        # Inicializa a superclasse
        pygame.sprite.Sprite.__init__(self)

        # Carrega a imagem de fundo
        self.image = pygame.image.load(path / 'imagens/wallpaper_estrelas.jpeg')

        # Obtém o retângulo que circunscreve a imagem
        self.rect = self.image.get_rect()