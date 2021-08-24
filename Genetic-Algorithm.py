import math
import random

file = open('imput.txt', 'r')
populationSize = int(file.readline())
generationNumber = file.readline()

x = []
valFitness = []
probability = []

def fitness(x):
    vFunction = (2 * math.exp(((-(x[0]) - 5) ** 2) / .5)) + (1.2 * math.exp(((-(x[0]) - 6) ** 2) / .9)) + (
        .9 * math.exp(((-(x[0]) - 4) ** 2) / 1.1)) + (1.5 * math.exp(((-(x[1]) - 1) ** 2) / 1)) + (
        1.2 * math.exp(((-(x[1]) - 2) ** 2) / 1)) + (1.3 *math.exp(((-(x[2]) - 3) ** 2) / .2)) + (
        .8 * math.exp(((-(x[3]) - 2) ** 2) / .3))
    return int(vFunction)

def roulette():
    vSum = sum(valFitness)
    for i in range(populationSize):
        r = round(random.uniform(0, vSum), 2)
        if (valFitness[i] >= r):
            drawn = i
    return drawn

def fProbability(valFitness):
    vSum = sum(valFitness)
    for i in range(populationSize):
        total = valFitness
        probability.append(total)
    return probability