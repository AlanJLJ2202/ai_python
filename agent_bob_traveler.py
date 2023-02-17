import math

cant_ubicaciones, bob_house = map(int, input().split())
print('CANT_UBICACIONES', cant_ubicaciones)
print('BOB_HOUSE', bob_house)
nueva_data = []

for i in range(cant_ubicaciones):
    id, x, y = map(int, input().split())
    nueva_data.append([id, x, y])


#df = pd.DataFrame(nueva_data, columns=['indice', 'x', 'y'])

# Mover las filas que coinciden con la condición a la primera posición
#df = pd.concat([df[df['indice'] == bob_house], df[df['indice'] != bob_house]]).reset_index(drop=True)

#Se calcula la matriz de distancias
#matriz_distancias = squareform((pdist(df[['x', 'y']])))

distancias = [[0.0 for j in range(cant_ubicaciones)] for i in range(cant_ubicaciones)]

for i in range(cant_ubicaciones):
    for j in range(cant_ubicaciones):
        dist = ((nueva_data[i][1] - nueva_data[j][1]) ** 2 +
                (nueva_data[i][2] - nueva_data[j][2]) ** 2) ** 0.5
        distancias[i][j] = dist

#Cada elemento de la matriz de distancias se redondea a el entero más cercano
for i in range(cant_ubicaciones):
     for j in range(len(distancias)):
        if distancias[i][j] != '--' and distancias[i][j] != 0.0:
            distancias[i][j] = int(distancias[i][j] + 0.5)
    
        # if distancias[i][j] != '--' and distancias[i][j] != 0.0:
        #     valor_nuevo = int(distancias[i][j] + 0.5)
        #     distancias[i][j] = int(distancias[i][j] + 0.5)


print(distancias)
     
# Definimos el punto inicial y lo agregamos a una lista de puntos visitados
punto_inicial = 0
puntos_visitados_lista = [bob_house]
distancia_recorrida = 0

# Definimos una función para encontrar el punto más cercano a un punto dado
def encontrar_vecino_mas_cercano(point, puntos_visitados):

    print('PUNTO INICIAL', point)

    # Calculamos las distancias entre el punto y todos los demás puntos
    distancia_a_todos = distancias[point-1][:]
    print(distancia_a_todos)

    # Eliminamos las distancias a los puntos que ya fueron visitados
    for i in puntos_visitados:
        distancia_a_todos[i-1] = 100

    print('DISTANCIA A TODOS', distancia_a_todos)
    segunda_lista = [i for i in distancia_a_todos if i != 0]
    print('INDEX', (distancia_a_todos.index(min(segunda_lista)))+1)
    vecino_mas_cercano = (distancia_a_todos.index(min(segunda_lista)))+1
    index_visitado = (distancia_a_todos.index(min(segunda_lista)))
    print('DISTANCIA', min(segunda_lista))
    distancia_recorrida = min(segunda_lista)

    print('---------------------------------')
    return vecino_mas_cercano, index_visitado, distancia_recorrida


# Iteramos sobre todos los puntos de la matriz de distancias
for i in range(cant_ubicaciones):
    # Encontramos el punto más cercano al último punto visitado
    nearest_neighbor, index, distancia_total = encontrar_vecino_mas_cercano(puntos_visitados_lista[-1], puntos_visitados_lista)
    # Agregamos el punto más cercano a la lista de puntos visitados
    if nearest_neighbor not in puntos_visitados_lista:
        puntos_visitados_lista.append(nearest_neighbor)
        distancia_recorrida += distancia_total

puntos_visitados_lista.insert(0, distancia_recorrida+distancias[puntos_visitados_lista[-1]-1][puntos_visitados_lista[0]-1])

for i in range(len(puntos_visitados_lista)):
    print(puntos_visitados_lista[i])







