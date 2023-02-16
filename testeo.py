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

# Mostrar el dataframe ordenado
print(df)


# Definir la función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(point1, point2):
    print('DISTANCIA EUCLIDIANA')
    print('PUNTO 1', point1[1])
    print('PUNTO 2', point2[1])

    return np.sqrt((point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)

# Crear una lista vacía para almacenar la ruta recorrida por el agente
route = []

# Definir la primera posición del agente como el punto de inicio y agregarlo a la ruta
start_point = df.iloc[0]
route.append(start_point.indice)
#print(start_point.indice)

dist_matrix = squareform(pdist(df[['x', 'y']]))
#print(dist_matrix)
#print('lenght', len(dist_matrix))
matriz_sin_ceros = np.ma.masked_equal(dist_matrix, 0)

print(matriz_sin_ceros)
sumatoria = 0

puntos_visitados = []
indice_actual = 0

#Distancia minima partiendo del punto 2

print('MINIMO', np.min(matriz_sin_ceros[indice_actual]))
print('INDICE DEL VALOR MENOR', np.argmin(matriz_sin_ceros[indice_actual]))

puntos_visitados.append(df.iloc[indice_actual].indice)

print('PUNTOS VISITADOS', puntos_visitados)



# for i in range(len(matriz_sin_ceros)):
    
#     print('i', i)
#     for j in range(len(matriz_sin_ceros)):
#         print(matriz_sin_ceros[i, j])

#     print('MINIMO', np.min(matriz_sin_ceros[i]))
#     sumatoria += np.min(matriz_sin_ceros[i])
#     print('INDICE DEL VALOR MENOR', np.argmin(matriz_sin_ceros[i]))

#     print('-----------------------')

# print('SUMATORIA', sumatoria)






# Mientras haya puntos sin visitar, buscar el punto más cercano al punto actual y agregarlo a la ruta
#visited_points = set()
#visited_points.add(start_point.indice)
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





'''
df_sub = df[df['indice'] != bob_house].reset_index(drop=True)
#print(df_sub)

dist_matrix = squareform(pdist(df_sub[['x', 'y']]))
print(dist_matrix)

mst = minimum_spanning_tree(dist_matrix)
print(mst)

#order = depth_first_order(mst, df_sub[df_sub['indice']==2].index[0])

#order = [df[df['indice']==2].index[0]] + [df_sub.index[i] for i in order]
#print(order)
'''
