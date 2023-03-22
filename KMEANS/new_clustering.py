import cv2
import numpy as np
import matplotlib.pyplot as plt

def kmeans(imagen, k, metrica_distancia):

    # Convertir a la imagen a RGB
    imagen = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Se remodela la imagen a una matriz de 2D de pixeles y 3 valores de color (RGB)
    pixel_values = image.reshape((-1, 3))

    # Se convierte a flotante
    pixel_values = np.float32(pixel_values)

    # Se inicializan los centroides aleatoriamente
    centroides = np.random.rand(k, 3) * 255

    # Se establecen los criterios de parada
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    
    # Asignar cada punto a su centroide más cercano
    controides_viejos = centroides + 1 # Se inicializa con un valor diferente para que entre al ciclo


    for i in range(200):

        if metrica_distancia == "euclidean":
            distances = np.linalg.norm(pixel_values - centroides[:, np.newaxis], axis=2)
        elif metrica_distancia == "manhattan":
            distances = np.sum(np.abs(pixel_values - centroides[:, np.newaxis]), axis=2)

        labels = np.argmin(distances, axis=0)

        # Actualizar los centroides
        for j in range(k):
            centroides[j] = np.mean(pixel_values[labels == j], axis=0)

        # Verificar el criterio de parada
        if np.allclose(centroides, controides_viejos):
            break
        controides_viejos = centroides.copy()


    # Convertir de vuelta a valores de 8 bits
    centros = np.uint8(centroides)

    # Aplanar la matriz de etiquetas
    labels = labels.flatten()

    # Convertir todos los píxeles al color del centroide correspondiente
    imagen_segmentada = centros[labels.flatten()]

    # Volver a darle forma a la imagen original
    imagen_segmentada = imagen_segmentada.reshape(image.shape)

    # Desactivar solo el cluster especificado (convertir el píxel en negro)
    imagen_enmascarada = np.copy(image)

    # Convertir a la forma de un vector de valores de píxeles
    imagen_enmascarada = imagen_enmascarada.reshape((-1, 3))

    # Cluster a desactivar
    cluster = 2
    imagen_enmascarada[labels == cluster] = [0, 0, 0]

    # Volver a darle forma a la imagen original
    imagen_enmascarada = imagen_enmascarada.reshape(image.shape)

    # Mostrar la imagen enmascarada
    plt.imshow(imagen_enmascarada)
    plt.show()

# Leer la imagen
image = cv2.imread("KMEANS/UP_small.png")

# Aplicar K-Means con k=3 y distancia euclidiana
kmeans(image, 2, "euclidean")




    