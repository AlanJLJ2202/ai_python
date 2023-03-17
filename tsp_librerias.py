import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform

#Se declaran la cantidad de ubicaciones
ubicaciones = 4

#Se declara de donde inicia el recorrido del agente viajero
bob_house = 3

#Se declara la matriz de distancias
data = [
        [1, 2, 6],
        [2, 2, 4],
        [3, 2, 1],
        [4, 2, 1],
    ]

df = pd.DataFrame(data, columns=['indice', 'x', 'y'])
#print(df)

# Mover las filas que coinciden con la condición a la primera posición
df = pd.concat([df[df['indice'] == bob_house], df[df['indice'] != bob_house]]).reset_index(drop=True)

#Se calcula la matriz de distancias
matriz_distancias = squareform((pdist(df[['x', 'y']])))

puntos_visitados = []
indice_actual = 0

for i in range(len(matriz_distancias)):
     for j in range(len(matriz_distancias)):
        if matriz_distancias[i, j] != '--' and matriz_distancias[i, j] != 0.0:
            valor_nuevo = int(matriz_distancias[i, j] + 0.5)
            matriz_distancias[i, j] = int(matriz_distancias[i, j] + 0.5)
            
            
print(matriz_distancias)

# Definimos el punto inicial y lo agregamos a una lista de puntos visitados
punto_inicial = 0
puntos_visitados = [punto_inicial]


# Definimos una función para encontrar el punto más cercano a un punto dado
def encontrar_vecino_mas_cercano(point, puntos_visitados):

    # Calculamos las distancias entre el punto y todos los demás puntos
    distancia_a_todos = matriz_distancias[point, :]
    print(distancia_a_todos)

    # Eliminamos los puntos que ya fueron visitados
    distancia_a_todos[puntos_visitados] = np.inf

    # Encontramos el índice del punto más cercano
    vecino_mas_cercano = np.argmin(distancia_a_todos)
    return vecino_mas_cercano


# Iteramos sobre todos los puntos de la matriz de distancias
for i in range(len(matriz_distancias)):

    print(puntos_visitados[-1])
    # Encontramos el punto más cercano al último punto visitado
    nearest_neighbor = encontrar_vecino_mas_cercano(puntos_visitados[-1], puntos_visitados)

    # Agregamos el punto más cercano a la lista de puntos visitados
    puntos_visitados.append(nearest_neighbor)


puntos = []
for point in puntos_visitados:
    if df.loc[point].indice not in puntos:
        puntos.append(df.loc[point].indice)


print(puntos)
print(puntos_visitados)

# Definir la función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(point1, point2):
     return np.sqrt((point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)

# Calculamos la sumatoria de las distancias entre los puntos visitados
sum_of_distances = 0
for i in range(1, len(puntos_visitados)):
    sum_of_distances += matriz_distancias[puntos_visitados[i-1], puntos_visitados[i]]


#Calcular la distancia total recorrida por el agente
total_distance = 0
for i in range(len(puntos_visitados)-1):
     total_distance += euclidean_distance(df.loc[puntos_visitados[i]], df.loc[puntos_visitados[i+1]])

for punto in puntos:
    print(punto)

print("Sumatoria de distancias recorridas:", int(total_distance))