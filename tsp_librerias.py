import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import depth_first_order



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

print("Sumatoria de distancias recorridas:", int(total_distance))

''''
for i in range(len(matriz_distancias)):
    print('ITERACION', i)
    print('INDICE ACTUAL', indice_actual)
    #indice_actual = np.argmin(matriz_distancias[i])
    #if df.loc[indice_actual].indice not in puntos_visitados:
        #puntos_visitados.append(df.loc[indice_actual].indice)
    print('-------------------------------------')
    #indice_actual = np.argmin(matriz_distancias[i])
    indice_actual = np.argmin(matriz_distancias[i])
    if df.loc[indice_actual].indice not in puntos_visitados:
        puntos_visitados.append(df.loc[indice_actual].indice)
            
            
        #indice_actual = np.argmin(matriz_distancias[i])
        #print('INDICE', df.loc[np.argmin(matriz_distancias[i])])
     
#print('SUMATORIA', sumatoria)
print(matriz_distancias)
print('PUNTOS VISITADOS', puntos_visitados)
'''

# Mientras haya puntos sin visitar, buscar el punto más cercano al punto actual y agregarlo a la ruta
#puntos_visitados = set()
#puntos_visitados.add(start_point.indice)
# print(len(df))


# puntos_visitados = []
# puntos_visitados.append(start_point.indice)

# closest_distance = np.inf
# closest_point = None
# current_point = df.loc[route[-1]]

# dist_matrix = squareform(pdist(df_sub[['x', 'y']]))
# print(dist_matrix)

# while len(puntos_visitados) < len(df):
    
    
#     for index, row in df.iterrows():
    
#         print('ROW', row.indice)
        

#         if row.indice not in puntos_visitados:
#             distance = euclidean_distance(current_point, row)

#             print('PUNTO ACTUAL', current_point.indice)
#             print('Distancia', distance)

#             closest_point = row.indice

#             # if distance < closest_distance:
#             #     closest_distance = distance
#             #     closest_point = row.indice
#             # elif distance == closest_distance and row.indice < closest_point:
#             #     closest_point = row.indice


#             puntos_visitados.append(closest_point)
#             print('PUNTOS VISITADOS', puntos_visitados)
#             route.append(closest_point)
#             print('route', route)
    

# # Agregar el punto de inicio a la ruta para completar el ciclo
# route.append(start_point.indice)

# # Calcular la distancia total recorrida por el agente
# total_distance = 0
# for i in range(len(route)-1):
#     total_distance += euclidean_distance(df.loc[route[i]], df.loc[route[i+1]])

# # Imprimir la ruta recorrida y la distancia total recorrida
# print('Ruta recorrida: ', route)
# print('Distancia total recorrida: ', total_distance)



'''
import matplotlib.pyplot as plt
plt.scatter(df['x'], df['y'])
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de puntos')
plt.show()
'''