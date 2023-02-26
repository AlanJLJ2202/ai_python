import operator
import random

import numpy as np
import math

from deap import base
from deap import benchmarks
from deap import creator
from deap import tools

import matplotlib.pyplot as plt

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Particle", list, fitness=creator.FitnessMin, speed=list,
                smin=None, smax=None, best=None)

def generate(size, pmin, pmax, smin, smax):
    part = creator.Particle(random.uniform(pmin, pmax) for _ in range(size)) 
    part.speed = [random.uniform(smin, smax) for _ in range(size)]
    part.smin = smin
    part.smax = smax
    return part


def updateParticle(part, best, phi1, phi2):

    # u1 = (random.uniform(0, phi1) for _ in range(len(part)))
    # u2 = (random.uniform(0, phi2) for _ in range(len(part)))
    # v_u1 = map(operator.mul, u1, map(operator.sub, part.best, part))
    # v_u2 = map(operator.mul, u2, map(operator.sub, best, part))

    phi1 = np.random.uniform(0, phi1)
    phi2 = np.random.uniform(0, phi2)

    cognitive = phi1 * np.subtract(part.speed, part)
    social = phi2 * np.subtract(best, part)
    part.speed = part.speed + cognitive + social


    #part.speed = list(map(operator.add, part.speed, map(operator.add, v_u1, v_u2)))
    for i, speed in enumerate(part.speed):
        if abs(speed) < part.smin:
            part.speed[i] = math.copysign(part.smin, speed)
        elif abs(speed) > part.smax:
            part.speed[i] = math.copysign(part.smax, speed)

    #finalmente actualizamos la particula 
    #part[:] = list(map(operator.add, part, part.speed))
    part[:] = part + part.speed
    print(part)



toolbox = base.Toolbox()
#pmin y pmax es de pocision
toolbox.register("particle", generate, size=2, pmin=-4, pmax=4, smin=-3, smax=3)
toolbox.register("population", tools.initRepeat, list, toolbox.particle)
toolbox.register("update", updateParticle, phi1=2.0, phi2=2.0)
toolbox.register("evaluate", benchmarks.sphere)

def main():
    pop = toolbox.population(n=100)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    logbook = tools.Logbook()
    logbook.header = ["gen", "evals"] + stats.fields

    GEN =  2000
    best = None

    fig, ax = plt.subplots()

    for g in range(GEN):
        x_coords = []
        y_coords = []

        for part in pop:
            part.fitness.values = toolbox.evaluate(part)
            if not part.best or part.best.fitness < part.fitness:
                part.best = creator.Particle(part)
                part.best.fitness.values = part.fitness.values
            if not best or best.fitness < part.fitness:
                best = creator.Particle(part)
                best.fitness.values = part.fitness.values

               
        for part in pop:
            toolbox.update(part, best)
            x_coords.append(part.best[0])
            y_coords.append(part.best[1])

        # Gather all the fitnesses in one list and print the stats
        logbook.record(gen=g, evals=len(pop), **stats.compile(pop))
        
        #print(logbook.stream)
        if g % 5 == 0:
            ax.clear()

            ax.set_xlim([-2, 2]) # Rango de valores para el eje x
            ax.set_ylim([-2, 2]) # Rango de valores para el eje y  

            #ax.set_xlim([-1, 1]) # Rango de valores para el eje x
            #ax.set_ylim([-1, 1]) # Rango de valores para el eje y  

            #ax.set_xlim([-0.5, 0.5]) # Rango de valores para el eje x
            #ax.set_ylim([-0.5, 0.5]) # Rango de valores para el eje y  

            #ax.set_xlim([-0.2, 0.2]) # Rango de valores para el eje x
            #ax.set_ylim([-0.2, 0.2]) # Rango de valores para el eje y  


            ax.set_facecolor('black')
            fig.patch.set_facecolor('black')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.tick_params(colors='white')
            ax.scatter(x_coords, y_coords, s=7, alpha=0.4, c=(1,1,1))
            plt.pause(0.1)
    plt.show()

    return pop, logbook, best


if __name__ == "__main__":
    pop, logbook, best = main()
    print(best)