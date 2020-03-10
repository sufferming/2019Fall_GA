# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 00:22:12 2019

@author: tc_chien
"""
import numpy as np
import math
import time
import random
import sGA_func as ga

"""
    Using GA to solve Funding Optimization Problem
"""
# PARAMETER SETTING
chromosom_len = 30;
population_size = int(4 * chromosom_len * math.log(chromosom_len));
#population_size = 4000;
generation =  30;
risk_type = "Low"
tic_run = time.time()

# Intialize population
print("Population")
population = np.zeros([population_size,chromosom_len],int)
for i in range(population_size):
    for j in range(chromosom_len):
        if random.random() > 0.5:
            population[i][j] = 1;
        else:
            population[i][j] = 0;

'''
# Cal Fitness
print("Cal fitness")
idx_norm, fitness = ga.cal_funding_reward(risk_type, population)                              ##
#print(fitness)

# Selection 
print("Selection = Parrents")
parrent = ga.selc_tournament(population,fitness)
#print(parrent)

# Crossover 
print("XO = Child = Next generation")
next_generation = ga.XO_pop_wise_shuffling(parrent)
#print(next_generation)

population = next_generation
'''

# Storage best fitness in every generation
his_best_fitness = []
his_weight = []

# GA run
for gen in range(generation):
    print("========================================")
    print("Generation:", gen)
    # Generate next offsprings
    tic1 = time.time()
    print("Cal fitness")
    idx_true, fitness = ga.cal_funding_reward(risk_type, population)                  ##
    best_match_idx = np.where(fitness == np.max(fitness))
    #his_best_fitness.append(idx_true[best_match_idx[0][0]] * [100000, 100000, 10000, 10000, 1000, 1])
    his_best_fitness.append(idx_true[best_match_idx[0][0]])
    his_weight.append(ga.get_weight(population[best_match_idx[0][0], :]))
    print("Selection = Parrents")
    parrent = ga.selc_tournament(population,fitness)
    print("XO = Child = Next generation")
    next_generation = ga.XO_pop_wise_shuffling(parrent)
    # Offspring -> Population
    population = next_generation
    print("Generation time: ", time.time() - tic1, " s")

# Display the final result
idx_true, fitness = ga.cal_funding_reward(risk_type, population)                              ##
best_match_idx = np.where(fitness == np.max(fitness))
his_best_fitness.append(idx_true[best_match_idx[0][0]])
his_weight.append(ga.get_weight(population[best_match_idx[0][0], :]))
print("Final ======================================")
print(population[best_match_idx[0][0], :])
print(ga.get_weight(population[best_match_idx[0][0], :]))
print(ga.get_idx(ga.get_weight(population[best_match_idx[0][0], :])))
print("Total time cost:", time.time() - tic_run, " s")
print("============================================")

# FIGURE
ga.result_plot(his_best_fitness, his_weight, risk_type)