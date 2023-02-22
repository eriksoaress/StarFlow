import random
import numpy as np
from constantes import *
raio_planeta = random.randint(20,60)
posicao_planeta = np.array([random.randint(400, int(1280-raio_planeta/2)), random.randint(int(raio_planeta/2), int(720-raio_planeta/2))])
raio_poeira = random.randint(100,200)
posicao_poeira = np.array([random.randint(int(raio_poeira/2) + 200, int(1280-raio_poeira/2)), random.randint(int(raio_poeira/2), int(720-raio_poeira/2))])
COR_1 = (255, 255, 255)
COR_2 = (255, 255, 255)
COR_3 = (255, 255, 255)
