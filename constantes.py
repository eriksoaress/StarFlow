from pathlib import Path
import numpy as np
WIDTH = 1280
HEIGHT = 720
FPS = 60
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
PURPLE = (74,20,140)
WHITE = (255,255,255)
color = [GREEN, RED, PURPLE]
posicao_inicial_estrela = np.array([300,360])
path = Path().cwd()