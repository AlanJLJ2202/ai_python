import numpy as np

# Definimos los pesos sinápticos y el bias
weights = np.array([0.5, 0.5])  # Pesos sinápticos para las entradas
bias = -0.7  # Bias

# Definimos la función de activación
def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0

# Definimos la función para calcular la salida de la neurona
def neuron(input_values):
    # Multiplicamos los valores de entrada por los pesos sinápticos y sumamos el resultado
    neuron_input = np.dot(input_values, weights) + bias
    
    # Aplicamos la función de activación
    neuron_output = step_function(neuron_input)
    
    return neuron_output

# Probamos la neurona con algunos valores de entrada
input_values = np.array([0, 1])  # Valores de entrada para la neurona
output = neuron(input_values)  # Calculamos la salida de la neurona
print(output)  # Imprimimos la salida de la neurona