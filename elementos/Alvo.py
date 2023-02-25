from imports import *
class Alvo(pygame.sprite.Sprite):
        '''Classe para criar o alvo'''
        def __init__(self):
            # Inicializa a classe pygame.sprite.Sprite
            pygame.sprite.Sprite.__init__(self)

            # Carrega a imagem do alvo e redimensiona para o tamanho desejado
            self.image = pygame.image.load(path / "imagens/Attack_2.png")
            self.image = pygame.transform.scale(self.image, (100,100))

            # Define a posição inicial do alvo
            self.rect = self.image.get_rect()
            self.rect.center = np.array([1230,HEIGHT/2])

                
        def update(self):
            '''Método para atualizar a posição do alvo e trocar sua imagem para criar animação'''

            # Atualiza a posição do alvo com uma posição aleatória na vertical
            self.rect.center = np.array([1230,random.randint(50, HEIGHT - 50) ])