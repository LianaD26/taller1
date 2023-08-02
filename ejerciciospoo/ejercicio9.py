import numpy as np
import random
def generar_matriz(fil, col):
    array = np.random.randint(10, size=(fil, col))
    print(array)
generar_matriz(4,6)