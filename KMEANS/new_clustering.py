import cv2
import numpy as np
import matplotlib.pyplot as plt


def extract_image(imagen):

    # Convertir a la imagen a RGB
    imagen = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Se remodela la imagen a una matriz de 2D de pixeles y 3 valores de color (RGB)
    pixel_values = imagen.reshape((-1, 3))

    print('PIXEL VALUES')
    print(pixel_values)
    # Se convierte a flotante
    # pixel_values = np.float32(pixel_values)

    # Se retorna los valores de pixeles
    return pixel_values



def kmeans(imagen, k, metrica_distancia):

    pixel_values = extract_image(imagen)

    # Se inicializan los centroides aleatoriamente
    centroides = np.random.rand(k, 3) * 255

    # Asignar cada punto a su centroide más cercano
    controides_viejos = centroides + 1 # Se inicializa con un valor diferente para que entre al ciclo

    update = True

    while(update):

        if metrica_distancia == "euclidean":
            distances = np.linalg.norm(pixel_values - centroides[:, np.newaxis], axis=2)
        elif metrica_distancia == "manhattan":
            distances = np.sum(np.abs(pixel_values - centroides[:, np.newaxis]), axis=2)

        labels = np.argmin(distances, axis=0)
    
        for j in range(k):
            centroides[j] = np.mean(pixel_values[labels == j], axis=0)

        # Verificar el criterio de parada
        if np.allclose(centroides, controides_viejos):
            print('entra al criterio de parada')
            break

        controides_viejos = centroides.copy()
        
        
    # Convertir de vuelta a valores de 8 bits
    centros = np.uint8(centroides)

    # Convertir todos los píxeles al color del centroide correspondiente
    imagen_segmentada = centros[labels]

    # Volver a darle forma a la imagen original
    imagen_segmentada = imagen_segmentada.reshape(image.shape)

    # Mostrar la imagen enmascarada
    plt.imshow(imagen_segmentada)
    plt.show()

# Leer la imagen
image = cv2.imread("KMEANS/UP_small.jpeg")

kmeans(image, 7, "euclidean")




    