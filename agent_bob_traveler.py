

import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean


#Se declaran la cantidad de ubicaciones
ubicaciones = 4

#Se declara de donde inicia el recorrido del agente viajero
bob_house = 2

#Se declara la matriz de distancias
data = [
        [1, 0, 7],
        [2, 4, 3],
        [3, 6, 1],
        [4, 5, 1],
    ]

df = pd.DataFrame(data, columns=['indice', 'x', 'y'])
print(df)

x = df['x'].values
y = df['y'].values

# Crear una matriz de puntos con las coordenadas x e y
points = np.column_stack((x, y))
print(points)

# Calcular la distancia Euclidiana entre todos los puntos
n = len(points)
#distances = np.zeros((n, n))
#for i in range(n):
#    for j in range(n):
#        distances[i, j] = euclidean(pd.to_numeric(points[i]), pd.to_numeric(points[j]))


# Las distancias euclidianas están almacenadas en la matriz "distances"
#print(distances)


'''
import math

# leer la entrada del usuario
n, s = map(int, input().split())

# almacenar los puntos en un diccionario
points = {}
for _ in range(n):
    i, x, y = map(int, input().split())
    points[i] = (x, y)

# calcular la distancia de Bob a cada punto y guardar el mínimo
min_distance = float('inf')
for i in points:
    if i == s:
        continue
    distance = math.sqrt((points[i][0] - points[s][0]) ** 2 + (points[i][1] - points[s][1]) ** 2)
    if distance < min_distance:
        min_distance = distance

# imprimir la distancia mínima
print(min_distance)
'''






