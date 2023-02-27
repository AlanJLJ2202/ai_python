#Instalar las librerias necesarias
import operator
import random

import numpy as np
import math

from deap import base
from deap import benchmarks
from deap import creator
from deap import tools

import matplotlib.pyplot as plt

#Se crea el tipo de dato particula, con el fitness y la velocidad, ademas de los valores minimos y maximos de la velocidad
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Particle", list, fitness=creator.FitnessMin, speed=list,
                smin=None, smax=None, best=None)

#Funcion para generar la particula, recibe el tamaño, el minimo y maximo de la posicion y la velocidad
def generate(size, pmin, pmax, smin, smax):
    part = creator.Particle(random.uniform(pmin, pmax) for _ in range(size)) 
    part.speed = [random.uniform(smin, smax) for _ in range(size)]
    part.smin = smin
    part.smax = smax
    return part


#Funcion para actualizar la particula
def updateParticle(part, best, phi1, phi2):

    #los valores de phi1 y phi2 son aleatorios
    phi1 = np.random.uniform(0, phi1)
    phi2 = np.random.uniform(0, phi2)

    #actualizamos la velocidad de la particula
    cognitive = phi1 * np.subtract(part.speed, part)
    social = phi2 * np.subtract(best, part)
    part.speed = part.speed + cognitive + social

    #se verifica que la velocidad no sea mayor a la maxima o menor a la minima
    for i, speed in enumerate(part.speed):
        if abs(speed) < part.smin:
            part.speed[i] = math.copysign(part.smin, speed)
        elif abs(speed) > part.smax:
            part.speed[i] = math.copysign(part.smax, speed)

    #finalmente actualizamos la particula 
    part[:] = part + part.speed
    print(part)


#Se crea la herramienta toolbox, se registran las funciones de generar, actualizar y evaluar
toolbox = base.Toolbox()

#pmin y pmax es de pocision, 
toolbox.register("particle", generate, size=2, pmin=-4, pmax=4, smin=-3, smax=3)
toolbox.register("population", tools.initRepeat, list, toolbox.particle)
toolbox.register("update", updateParticle, phi1=2.0, phi2=2.0)
toolbox.register("evaluate", benchmarks.sphere)

def main():
    pop = toolbox.population(n=100)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    #Se registran las estadisticas que se quieren obtener
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    logbook = tools.Logbook()
    logbook.header = ["gen", "evals"] + stats.fields

    # número de generaciones (Puedes cambiarlo para ver como se comporta)
    GEN =  2000
    best = None

    # se crea la figura y los ejes para la gráfica
    fig, ax = plt.subplots()

    for g in range(GEN):
        # se crean dos colecciones vacías para guardar los valores de X y de Y
        x_coords = []
        y_coords = []

        # Se evalua cada particula en la poblacion, se actualiza el mejor de la particula y el mejor de la poblacion
        for part in pop:
            part.fitness.values = toolbox.evaluate(part)
            if not part.best or part.best.fitness < part.fitness:
                part.best = creator.Particle(part)
                part.best.fitness.values = part.fitness.values
            if not best or best.fitness < part.fitness:
                best = creator.Particle(part)
                best.fitness.values = part.fitness.values

        # Se actualiza la velocidad y la posicion de cada particula, se agregan los valores de X y Y a las colecciones
        for part in pop:
            toolbox.update(part, best)
            x_coords.append(part.best[0])
            y_coords.append(part.best[1])

        # Se actualiza el logbook, se agregan los valores de la generacion actual
        logbook.record(gen=g, evals=len(pop), **stats.compile(pop))
        
        #print(logbook.stream)

        # cada cinco generaciones se actualizan las partículas en la gráfica
        if g % 5 == 0:
            ax.clear()

            # intenta calándole con el primer rango y después va comentando y les comentando para que pruebes en diferentes medidas
            ax.set_xlim([-2, 2]) # Rango de valores para el eje x
            ax.set_ylim([-2, 2]) # Rango de valores para el eje y  

            #ax.set_xlim([-1, 1]) # Rango de valores para el eje x
            #ax.set_ylim([-1, 1]) # Rango de valores para el eje y  

            #ax.set_xlim([-0.5, 0.5]) # Rango de valores para el eje x
            #ax.set_ylim([-0.5, 0.5]) # Rango de valores para el eje y  

            #ax.set_xlim([-0.2, 0.2]) # Rango de valores para el eje x
            #ax.set_ylim([-0.2, 0.2]) # Rango de valores para el eje y  


            #esto es más para el estilo de la gráfica asignar un fondo negro y los puntos blancos
            ax.set_facecolor('black')
            fig.patch.set_facecolor('black')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.tick_params(colors='white')
            ax.scatter(x_coords, y_coords, s=7, alpha=0.4, c=(1,1,1))
            plt.pause(0.1)
    plt.show()

    #Se retorna la poblacion, el logbook y el mejor
    return pop, logbook, best


if __name__ == "__main__":
    pop, logbook, best = main()
    print(best)