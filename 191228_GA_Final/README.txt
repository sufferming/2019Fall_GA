調整風險
    sGA_func.py
	def cal_funding_reward_LR(pop):
	    ...
            fitness[l] = idx_norm[l][5] * 0.01 + np.sum(idx_norm[l][0:4]) * 0.99 / 5
    	    ...
	
	調整 0.01 and 0.99


	def cal_funding_reward_MR(pop) / def cal_funding_reward_HR(pop)  同理

