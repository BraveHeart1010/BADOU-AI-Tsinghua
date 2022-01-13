# -*- coding: utf-8 -*-
"""
Aim: 最小二乘法拟合数据
Author: 祁朝阳
Data: 2021.12.27
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import pandas as pd

sales=pd.read_csv('train_data.csv',sep='\s*,\s*',engine='python')  #读取CSV
X = sales['X'].values
Y = sales['Y'].values

def Fun(p, x):
    # 定义函数：y=kx + b
    k,b = p
    return k*x+b

def error(p, x, y):
    # 定义残差，输出 (kx-b) - y
    return Fun(p,x)-y


def main():
    # 定义初始参数，这里认为y=2x+1
    p0 = [2,1]
    
    # 最小二乘
    para = leastsq(error, p0, args=(X,Y))
    # 输出拟合后的曲线方程：
    print(para[0])
    print('The fitted function is: y = {0}*x + {1}'.format(para[0][0], para[0][1]))


if __name__=='__main__':
    main()

