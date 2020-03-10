# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:51:56 2019

@author: tc_chien
"""
import numpy as np
import math
import matplotlib.pyplot

import new_vision as nv
GSPC_path = "GSPC.csv"
SP_path = "SP500BDT.csv"
USDX_path = "USDX.csv"

def cal_funding_reward(risk_type, pop):
    if risk_type == "High":
        idx_true, fitness = cal_funding_reward_HR(pop)
        print("H")
    elif risk_type == "Midium":
        idx_true, fitness = cal_funding_reward_MR(pop)
        print("M")
    elif risk_type == "Low":
        idx_true, fitness = cal_funding_reward_LR(pop)
        print("L")
    else:
        idx_true, fitness = cal_funding_reward_v1(pop)
        print("D")
    return idx_true, fitness

def cal_funding_reward_v1(pop):
    fitness = np.zeros([pop.shape[0], 1], float)
    idx_mtr = np.zeros([pop.shape[0], 6], float)
    idx_norm = np.zeros([pop.shape[0], 6], float)
    for i in range(pop.shape[0]):
        a = ""; b = ""; c = ""
        for j in range(10):
            a = a + str(pop[i, j])
            b = b + str(pop[i, j + 10])
            c = c + str(pop[i, j + 20])
        w_a = int(a,2)
        w_b = int(b,2)
        w_c = int(c,2)
        check_one = w_a + w_b + w_c
        w_GSPC = w_a / check_one
        w_SP = w_b / check_one
        w_USDX = w_c / check_one
        idx_mtr[i,:] = nv.first_fund(GSPC_path,SP_path,USDX_path,w_GSPC,w_SP,w_USDX).__call__(GSPC_path,SP_path,USDX_path,w_GSPC,w_SP,w_USDX)
    for k in range (idx_mtr.shape[1]):
        if (idx_mtr[:,k].max() - idx_mtr[:,k].min()) == 0:
            idx_norm[:,k] = 1
        else:
            idx_norm[:,k] = (idx_mtr[:,k] - idx_mtr[:,k].min())/ (idx_mtr[:,k].max() - idx_mtr[:,k].min())
    fitness = np.sum(idx_norm, axis = 1)
    return idx_mtr, fitness

def cal_funding_reward_HR(pop):
    fitness = np.zeros([pop.shape[0], 1], float)
    idx_mtr = np.zeros([pop.shape[0], 6], float)
    idx_norm = np.zeros([pop.shape[0], 6], float)
    for i in range(pop.shape[0]):
        a = ""; b = ""; c = ""
        for j in range(10):
            a = a + str(pop[i, j])
            b = b + str(pop[i, j + 10])
            c = c + str(pop[i, j + 20])
        w_a = int(a,2)
        w_b = int(b,2)
        w_c = int(c,2)
        check_one = w_a + w_b + w_c
        w_GSPC = w_a / check_one
        w_SP = w_b / check_one
        w_USDX = w_c / check_one
        idx_mtr[i,:] = nv.first_fund(GSPC_path,SP_path,USDX_path,w_GSPC,w_SP,w_USDX).__call__(GSPC_path,SP_path,USDX_path,w_GSPC,w_SP,w_USDX)
    for k in range (idx_mtr.shape[1]):
        if (idx_mtr[:,k].max() - idx_mtr[:,k].min()) == 0:
            idx_norm[:,k] = 1
        else:
            idx_norm[:,k] = (idx_mtr[:,k] - idx_mtr[:,k].min())/ (idx_mtr[:,k].max() - idx_mtr[:,k].min())
    for l in range(pop.shape[0]):
        fitness[l] = idx_norm[l][5] * 0.8 + np.sum(idx_norm[l][0:4]) * 0.2 / 5
    return idx_mtr, fitness
	
	
def cal_funding_reward_MR(pop):
    fitness = np.zeros([pop.shape[0], 1], float)
    idx_mtr = np.zeros([pop.shape[0], 6], float)
    idx_norm = np.zeros([pop.shape[0], 6], float)
    for i in range(pop.shape[0]):
        a = ""; b = ""; c = ""
        for j in range(10):
            a = a + str(pop[i, j])
            b = b + str(pop[i, j + 10])
            c = c + str(pop[i, j + 20])
        w_a = int(a,2)
        w_b = int(b,2)
        w_c = int(c,2)
        check_one = w_a + w_b + w_c
        w_GSPC = w_a / check_one
        w_SP = w_b / check_one
        w_USDX = w_c / check_one
        idx_mtr[i,:] = nv.first_fund(GSPC_path,SP_path,USDX_path,w_GSPC,w_SP,w_USDX).__call__(GSPC_path,SP_path,USDX_path,w_GSPC,w_SP,w_USDX)
    for k in range (idx_mtr.shape[1]):
        if (idx_mtr[:,k].max() - idx_mtr[:,k].min()) == 0:
            idx_norm[:,k] = 1
        else:
            idx_norm[:,k] = (idx_mtr[:,k] - idx_mtr[:,k].min())/ (idx_mtr[:,k].max() - idx_mtr[:,k].min())
    for l in range(pop.shape[0]):
        fitness[l] = idx_norm[l][5] * 0.2 + np.sum(idx_norm[l][0:4]) * 0.8 / 5
    return idx_mtr, fitness
	
def cal_funding_reward_LR(pop):
    fitness = np.zeros([pop.shape[0], 1], float)
    idx_mtr = np.zeros([pop.shape[0], 6], float)
    idx_norm = np.zeros([pop.shape[0], 6], float)
    for i in range(pop.shape[0]):
        a = ""; b = ""; c = ""
        for j in range(10):
            a = a + str(pop[i, j])
            b = b + str(pop[i, j + 10])
            c = c + str(pop[i, j + 20])
        w_a = int(a,2)
        w_b = int(b,2)
        w_c = int(c,2)
        check_one = w_a + w_b + w_c
        w_GSPC = w_a / check_one
        w_SP = w_b / check_one
        w_USDX = w_c / check_one
        idx_mtr[i,:] = nv.first_fund(GSPC_path,SP_path,USDX_path,w_GSPC,w_SP,w_USDX).__call__(GSPC_path,SP_path,USDX_path,w_GSPC,w_SP,w_USDX)
    for k in range (idx_mtr.shape[1]):
        if (idx_mtr[:,k].max() - idx_mtr[:,k].min()) == 0:
            idx_norm[:,k] = 1
        else:
            idx_norm[:,k] = (idx_mtr[:,k] - idx_mtr[:,k].min())/ (idx_mtr[:,k].max() - idx_mtr[:,k].min())
    for l in range(pop.shape[0]):
        #fitness[l] = idx_norm[l][5] * (1/(6*2)) + np.sum(idx_norm[l][0:4]) * (1 - (1/(6*2))) / 5
        fitness[l] = idx_norm[l][5] * 0.01 + np.sum(idx_norm[l][0:4]) * 0.99 / 5
    return idx_mtr, fitness

def cal_reward_fitness_test(pop):
    fitness = np.zeros([pop.shape[0], 1], float)
    for i in range(pop.shape[0]):
        a = ""; b = ""; c = ""
        for j in range(10):
            a = a + str(pop[i, j])
            b = b + str(pop[i, j + 10])
            c = c + str(pop[i, j + 20])
        w_a = int(a,2)
        w_b = int(b,2)
        w_c = int(c,2)
        check_one = w_a + w_b + w_c
        w_a = w_a / check_one
        w_b = w_b / check_one
        w_c = w_c / check_one
        fitness[i] = -1 * (pow((w_a - 0.001),2) + pow((w_b - 0.888),2) + pow((w_c - 0.111),2))
    return fitness

def get_weight(chromosome):
    for i in range(chromosome.shape[0]):
        a = ""; b = ""; c = ""
        for j in range(10):
            a = a + str(chromosome[j])
            b = b + str(chromosome[j + 10])
            c = c + str(chromosome[j + 20])
        w_a = int(a,2)
        w_b = int(b,2)
        w_c = int(c,2)
        check_one = w_a + w_b + w_c
        w_a = w_a / check_one
        w_b = w_b / check_one
        w_c = w_c / check_one
        return [w_a, w_b, w_c]
    
def get_idx(weight):
    idx = nv.first_fund(GSPC_path,SP_path,USDX_path,weight[0],weight[1],weight[2]).__call__(GSPC_path,SP_path,USDX_path,weight[0], weight[1], weight[2])
    return idx

def result_plot(his_best_fitness, his_weight, risk_type):
    # Resolution setting
    matplotlib.rcParams['figure.figsize'] = (16.0, 9.0) # 设置figure_size尺寸
    matplotlib.rcParams['image.interpolation'] = 'nearest' # 设置 interpolation style
    matplotlib.rcParams['image.cmap'] = 'gray' # 设置 颜色 style
    matplotlib.rcParams['savefig.dpi'] = 300 #图片像素
    matplotlib.rcParams['figure.dpi'] = 300 #分辨率
    matplotlib.rcParams['font.size'] = 6 
    matplotlib.rcParams['axes.labelsize'] = 6 
    matplotlib.rcParams['legend.fontsize'] = 6 
    matplotlib.rcParams['figure.autolayout'] = True
    matplotlib.rcParams['axes.grid'] = False
    matplotlib.rcParams['legend.loc'] = 'upper right'
    
    # plot
    his_idx = np.array(his_best_fitness)
    gen = his_idx.shape[0] - 1
    his_w = np.array(his_weight)
    matplotlib.pyplot.figure()
    matplotlib.pyplot.subplot(3,1,1)
    matplotlib.pyplot.title(risk_type + " risk type " + "Gen:" + str(len(his_best_fitness) - 1) + "\n" + str((his_w)[his_w.shape[0] - 1, :]))
    matplotlib.pyplot.plot(np.array(his_weight)[:,0])
    matplotlib.pyplot.plot(np.array(his_weight)[:,1])
    matplotlib.pyplot.plot(np.array(his_weight)[:,2])
    matplotlib.pyplot.legend(["GSPC", "SP500", "USDX"])
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Weights")
    matplotlib.pyplot.subplot(3,3,4)
    matplotlib.pyplot.plot(his_idx[:, 0])
    matplotlib.pyplot.text(gen, his_idx[gen, 0], '%.3f' % his_idx[gen, 0])
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Sharp")
    matplotlib.pyplot.subplot(3,3,5)
    matplotlib.pyplot.plot(his_idx[:, 1])
    matplotlib.pyplot.text(gen, his_idx[gen, 1], '%.3f' % his_idx[gen, 1])
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Sortino")
    matplotlib.pyplot.subplot(3,3,6)
    matplotlib.pyplot.plot(his_idx[:, 2])
    matplotlib.pyplot.text(gen, his_idx[gen, 2], '%.3f' % his_idx[gen, 2])
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Excess")
    matplotlib.pyplot.subplot(3,3,7)
    matplotlib.pyplot.plot(his_idx[:, 3])
    matplotlib.pyplot.text(gen, his_idx[gen, 3], '%.3f' % his_idx[gen, 3])
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("VaR")
    matplotlib.pyplot.subplot(3,3,8)
    matplotlib.pyplot.plot(his_idx[:, 4])
    matplotlib.pyplot.text(gen, his_idx[gen, 4], '%.3f' % his_idx[gen, 4])
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("E on Var")
    matplotlib.pyplot.subplot(3,3,9)
    matplotlib.pyplot.plot(his_idx[:, 5])
    matplotlib.pyplot.text(gen, his_idx[gen, 5], '%.3f' % his_idx[gen, 5])
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Gains")
    matplotlib.pyplot.show()
    return 0;
    
def cal_oneMAX_fitness(pop):
    fitness = np.zeros([pop.shape[0], 1], int)
    for i in range(pop.shape[0]):
        fitness[i] = np.sum(pop[i,:])
    return fitness

def selc_tournament(pop,fitness):
    # Create pool
    selection_pressure = 2
    tournament_pool = np.array([], int)
    for i in range(selection_pressure):
        temp_pool = np.arange(pop.shape[0])
        np.random.shuffle(temp_pool)
        tournament_pool = np.append(tournament_pool, temp_pool)
    # Choose the winner (parents for next generation)
    new_population = pop
    # print(tournament_pool.shape)
    for i in range(pop.shape[0]):
        winner_idx = tournament_pool[2*i]
        if (fitness[tournament_pool[2*i]] < fitness[tournament_pool[2*i + 1]]):
            winner_idx = tournament_pool[2*i + 1]
        new_population[i, :] = pop[winner_idx,:]
    return new_population
    
def XO_pop_wise_shuffling(parrent):
    child = parrent
    for i in range(parrent.shape[1]):
        shuffle_col = parrent[:, i]
        np.random.shuffle(shuffle_col)
        child[:, i] = shuffle_col
 #       for j in range(parrent.shape[0]):
 #           child[j,i] = shuffle_col[j]
    return child

    