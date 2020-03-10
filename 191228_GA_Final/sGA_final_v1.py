# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:40:12 2019

@author: tc_chien
"""
import numpy as np
import math
import matplotlib.pyplot
import time
import random
import sGA_func as ga

"""
    Using GA to solve oneMax Problem
"""
# PARAMETER SETTING
chromosom_len = 30;
population_size = int(4 * chromosom_len * math.log(chromosom_len));
#population_size = 4000;
generation =  10;

# Intialize population
population = np.zeros([population_size,chromosom_len],int)
for i in range(population_size):
    for j in range(chromosom_len):
        if random.random() > 0.5:
            population[i][j] = 1;
        else:
            population[i][j] = 0;
print("Population")
#print(population)

# Cal Fitness
fitness = ga.cal_reward_fitness_test(population)
#print(fitness)

# Selection 
parrent = ga.selc_tournament(population,fitness)
print("After selection = Parrents")
#print(parrent)

# Crossover 
next_generation = ga.XO_pop_wise_shuffling(parrent)
print("After XO = Child = Next generation")
#print(next_generation)

population = next_generation

# Storage best fitness in every generation
his_best_fitness = []

# GA run
for gen in range(generation):
    # Generate next offsprings
    tic1 = time.time()
    fitness = ga.cal_reward_fitness_test(population)
    parrent = ga.selc_tournament(population,fitness)
    next_generation = ga.XO_pop_wise_shuffling(parrent)

    # Display the best chromosome
    fitness = ga.cal_reward_fitness_test(next_generation)
    best_match_idx = np.where(fitness == np.max(fitness))
    print("Generation:", gen)
    print(next_generation[best_match_idx[0][0], :])
    print(fitness[best_match_idx[0][0]])
    print("Period",  time.time()-tic1)
    print("===========================",)
    his_best_fitness.append(fitness[best_match_idx[0][0]])

  
    # Offspring -> Population
    population = next_generation

# Display the final result
fitness = ga.cal_reward_fitness_test(population)
best_match_idx = np.where(fitness == np.max(fitness))
print("Final")
print(population[best_match_idx[0][0], :])
print(ga.get_weight(population[best_match_idx[0][0], :]))
print(fitness[best_match_idx[0][0]])

# FIGURE
# Resolution setting
matplotlib.rcParams['figure.figsize'] = (16.0, 9.0) # 设置figure_size尺寸
matplotlib.rcParams['image.interpolation'] = 'nearest' # 设置 interpolation style
matplotlib.rcParams['image.cmap'] = 'gray' # 设置 颜色 style
matplotlib.rcParams['savefig.dpi'] = 300 #图片像素
matplotlib.rcParams['figure.dpi'] = 300 #分辨率

# plot
matplotlib.pyplot.plot(his_best_fitness)
matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Fitness")
matplotlib.pyplot.show()