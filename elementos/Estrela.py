from imports import *
class Estrela(pygame.sprite.Sprite):
        '''Classe para criar a estrela, o objeto que disparará no alvo'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            # Carrega a imagem da estrela e redimensiona para o tamanho desejado
            self.image = pygame.image.load(path / "imagens/estrela_padrao.png")
            self.image = pygame.transform.scale(self.image, (30,30))
            
            self.rect = self.image.get_rect()

            #Posição inicial da estrela
            self.rect.centerx = posicao_inicial_estrela[0]
            self.rect.centery = posicao_inicial_estrela[1]


        def update(self, velocidade ,atingiu, estrela=''):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
            if not estrela == '' :
                self.image = pygame.image.load(path / f"imagens/{estrela}.png")
                self.image = pygame.transform.scale(self.image, (30,30))
                # Definindo a posição
                self.rect = self.image.get_rect()
                self.rect.centerx = posicao_inicial_estrela[0]
                self.rect.centery = posicao_inicial_estrela[1]

            # Se a estrela colidir com o alvo, ela volta para a posição inicial
            if atingiu:
                self.rect.centerx = posicao_inicial_estrela[0]
                self.rect.centery = posicao_inicial_estrela[1]

            # Se a estrela sair da tela, ela volta para a posição inicial
            if self.rect.centerx > 1310 or self.rect.centerx < -30 or self.rect.centery > 750 or self.rect.centery < -30:
                self.rect.centerx =posicao_inicial_estrela[0]
                self.rect.centery = posicao_inicial_estrela[1]

                return True
            # Nova posição da estrela