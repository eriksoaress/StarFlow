from imports import *

    
class Planeta(pygame.sprite.Sprite):
        '''Classe para alterar a velocidade de lançamento dos projéteis que a estrela arremessa'''
        def __init__(self,raio, posicao):
            pygame.sprite.Sprite.__init__(self)

            # Carrega a imagem do planeta e ajusta seu tamanho
            self.image = pygame.image.load(path / f"imagens/planeta.png")
            self.image = pygame.transform.scale(self.image, (raio,raio))

            # Define a posição do planeta na tela
            self.rect = self.image.get_rect()
            self.rect.centerx = posicao[0]
            self.rect.centery = posicao[1]
            
        def update(self, state):
            # Calcula o vetor da estrela ao planeta e a direção da gravidade
            vetor_planeta_estrela = np.array([self.rect.centerx, self.rect.centery]) - np.array([state['estrela'].rect.centerx, state['estrela'].rect.centery])
            direcao_gravidade = vetor_planeta_estrela / np.linalg.norm(vetor_planeta_estrela)
            
            # Calcula a força gravitacional do planeta sobre a estrela
            DT = G/np.linalg.norm(vetor_planeta_estrela)**2
            gravidade = DT * direcao_gravidade

            # Aplica a força gravitacional na velocidade da estrela
            if pygame.sprite.spritecollide(state['estrela'], state['poeiras'], False) : # Verifica se a estrela colidiu com a poeira para aplicar o atrito
                state['velocidade'] = state['velocidade']*0.98 +  gravidade
            else:
                state['velocidade'] = state['velocidade'] +  gravidade

            
             # Atualiza a posição da estrela de acordo com sua velocidade
            state['velocidade']  = state['velocidade'] +  gravidade
            state['estrela'].rect.centerx = state['estrela'].rect.centerx +  0.1*state['velocidade'][0]
            state['estrela'].rect.centery = state['estrela'].rect.centery +  0.1*state['velocidade'][1]