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
MAX_X_estrela = posicao_inicial_estrela[0] + 300  # posição x máxima
MIN_X_estrela = posicao_inicial_estrela[0] - 300  # posição x mínima
MAX_Y_estrela = posicao_inicial_estrela[1] + 300  # posição y máxima
MIN_Y_estrela = posicao_inicial_estrela[1] - 300  # posição y mínima
G = 20000
SURFACE_COLOR = (167, 255, 100)