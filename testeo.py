import pandas as pd
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
print(df)


df_sub = df[df['indice'] != bob_house].reset_index(drop=True)
#print(df_sub)

dist_matrix = squareform(pdist(df_sub[['x', 'y']]))
#print(dist_matrix)

mst = minimum_spanning_tree(dist_matrix)
print(mst)

order = depth_first_order(mst, df_sub[df_sub['indice']==2].index[0])

#order = [df[df['indice']==2].index[0]] + [df_sub.index[i] for i in order]
print(order)