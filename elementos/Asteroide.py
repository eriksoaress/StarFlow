
from imports import *

class Asteroide(pygame.sprite.Sprite):
    '''Classe para criar os asteroides e movê-los em torno do planeta'''
    def __init__(self,raio, posicao, angle, increment):
        pygame.sprite.Sprite.__init__(self)
        # Carregando a imagem do asteroide e escalonando
        self.image = pygame.image.load(path / f'imagens/asteroide{random.randint(1,2)}.png')
        self.image = pygame.transform.scale(self.image, (raio,raio))
        # Definindo a posição do asteroide
        self.rect = self.image.get_rect()
        self.rect.centerx = posicao[0] + 200
        self.rect.centery = posicao[1] 
        self.angle = angle
        self.increment = increment

    def update(self, posicao):
        # Atualizando a posição do asteroide de acordo com o ângulo e a posição do planeta
        self.rect.centerx = posicao[0]  + 100*math.cos(math.radians(self.angle)) 
        self.rect.centery = posicao[1] + 100*math.sin(math.radians(self.angle))
        self.angle = self.angle + self.increment
        