import random
import numpy as np
from constantes import *
raio_planeta = random.randint(20,80)
posicao_planeta = np.array([random.randint(int(raio_planeta/2), int(1280-raio_planeta/2)), random.randint(int(raio_planeta/2), int(720-raio_planeta/2))])
