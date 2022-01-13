# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 22:40:11 2022

@author: BraveHeart
"""
import pandas as pd
import scipy.linalg as la
import numpy as np
import matplotlib.pyplot as plt


sales=pd.read_csv('train_data.csv',sep='\s*,\s*',engine='python')  #读取CSV
X=sales['X'].values    #存csv的第一列
Y=sales['Y'].values    #存csv的第二列

# function is y = a0 + a1*x
A = np.vstack([X**0, X**1])
A = A.T     #计算矩阵

sol, r, rank, s = la.lstsq(A,Y)
print('a0 = ', sol[0])
print('a1 = ',sol[1])

y_fit = sol[0] + sol[1]*X

# plot image
fig, ax = plt.subplots(figsize = (12,8))
ax.plot(X,Y, 'ro',alpha=0.5, label='Simulated data')
ax.plot(X, y_fit, 'b-',lw=2, label='Fitted curve')
ax.set_xlabel('x', fontsize=18)
ax.set_ylabel('y', fontsize=18)
ax.legend(loc=2)
plt.show()







