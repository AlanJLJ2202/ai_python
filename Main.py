import math
def _main() -> None:
  cant_ubicaciones, bob_house = map(int, input().split())
  nueva_data = []

  for i in range(cant_ubicaciones):
      id, x, y = map(int, input().split())
      nueva_data.append([id, x, y])

  distancias = [[0.0 for j in range(cant_ubicaciones)] for i in range(cant_ubicaciones)]

  for i in range(cant_ubicaciones):
      for j in range(cant_ubicaciones):
          dist = ((nueva_data[i][1] - nueva_data[j][1]) ** 2 +
                  (nueva_data[i][2] - nueva_data[j][2]) ** 2) ** 0.5
          distancias[i][j] = dist

  for i in range(cant_ubicaciones):
      for j in range(len(distancias)):
          if distancias[i][j] != 0.0:
              distancias[i][j] = int(distancias[i][j] + 0.5)

  puntos_visitados_lista = [bob_house]
  distancia_recorrida = 0

  def encontrar_vecino_mas_cercano(point, puntos_visitados):
      distancia_a_todos = distancias[point-1][:]
      for i in puntos_visitados:
          distancia_a_todos[i-1] = math.inf
      
      segunda_lista = [i for i in distancia_a_todos if i != math.inf]
      if len(segunda_lista) != 0:
        vecino_mas_cercano = (distancia_a_todos.index(min(segunda_lista)))+1
        distancia_recorrida = min(segunda_lista)
        return vecino_mas_cercano, distancia_recorrida
      else:
        return 0, 0


  for i in range(cant_ubicaciones):
      nearest_neighbor, distancia_total = encontrar_vecino_mas_cercano(puntos_visitados_lista[-1], puntos_visitados_lista)
      if nearest_neighbor not in puntos_visitados_lista and nearest_neighbor != 0:
          puntos_visitados_lista.append(nearest_neighbor)
          distancia_recorrida += distancia_total
      
  puntos_visitados_lista.insert(0, int(distancia_recorrida+distancias[puntos_visitados_lista[-1]-1][puntos_visitados_lista[0]-1]))

  for i in range(len(puntos_visitados_lista)):
      print(puntos_visitados_lista[i])
 
  pass

if __name__ == '__main__':
  _main()

