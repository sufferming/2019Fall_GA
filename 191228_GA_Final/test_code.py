# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 23:37:37 2019

@author: tc_chien
"""

import new_vision as nv

w_GSPC = 0.5
w_SP = 0.3
w_USDX = 0.2
GSPC_path = "GSPC.csv"
SP_path = "SP500BDT.csv"
USDX_path = "USDX.csv"
idx = nv.first_fund(GSPC_path,SP_path,USDX_path,w_GSPC,w_SP,w_USDX).__call__(GSPC_path,SP_path,USDX_path,w_GSPC,w_SP,w_USDX)
print(idx)

# idx = [out_dic['sharp'], out_dic['sortino'], out_dic['excess'], out_dic['VAR'], out_dic['E on VaR']]
# np.append(idx, out_dic['history'][0]['unrealized gains'][len(out_dic['history'][0]['unrealized gains'])-1])
# print(idx)
