from imports import *

class Poeira(pygame.sprite.Sprite):
        '''Classe para alterar as propriedades das poeiras'''
        def __init__(self,largura,altura, posicao):
            pygame.sprite.Sprite.__init__(self)
            # Carrega a imagem da poeira e ajusta o tamanho
            self.image = pygame.image.load(path / "imagens/poeira.png")
            self.image = pygame.transform.scale(self.image, (largura, altura))

            # Define a posição inicial da poeira
            self.rect = self.image.get_rect()
            self.rect.centerx = posicao[0]
            self.rect.centery = posicao[1]
            
        def update(self):
            # Define uma nova posição aleatória para a poeira
            self.rect.centery = self.rect.centery + 1
            #self.rect.center = np.array([random.randint(int(variaveis.raio_poeira/2), int(1280-variaveis.raio_poeira/2)), random.randint(int(variaveis.raio_poeira/2), int(720-variaveis.raio_poeira/2))])
            if self.rect.centery > 720:
                self.rect.centery = -30
                self.rect.centerx = random.randint(int(variaveis.raio_poeira/2) +400, int(1280-variaveis.raio_poeira/2))