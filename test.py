import pandas as pd
import numpy as np
from scipy.spatial import distance

with open("kroA100.tsp") as f:
        content = f.readlines()

data = []
for line in content:
    if line.startswith("EOF"):
        break
    values = line.strip().split()
    lista_interna = []
    data.append([values[1], values[2]])


#1era Manera de hacerlo
matriz = np.array(data)

# Calcular las distancias euclidianas entre cada par de puntos
num_ciudades = matriz.shape[0]
distances = np.zeros((num_ciudades, num_ciudades))

for i in range(num_ciudades):
    for j in range(i+1, num_ciudades):
        distances[i, j] = np.linalg.norm(pd.to_numeric(matriz[i]) - pd.to_numeric(matriz[j]))
        distances[j, i] = distances[i, j]

# Las distancias euclidianas están almacenadas en la matriz "distances"
print(distances)

'''
#2da. Manera de hacerlo
df = pd.DataFrame(data)

#df = df.drop("index", axis=1)

df = df.astype(float)

df = df.values
print(df)

distances = distance.cdist(df, df, 'euclidean')
print(distances)
'''