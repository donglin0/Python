from numpy import array
from numpy.random import normal, randint
#使用List来创造一组数据
#data = [1, 2, 3]
#使用ndarray来创造一组数据
data = array([1, 2, 2, 2, 3])
#创造一组服从正态分，布的定量数据
#data = normal(0, 10, size=10)
#创造一组服从均匀分布的定性数据
#data = randint(0, 10, size=10)

from numpy import mean, median

#计算均值
print(mean(data))
#计算中位数
print(median(data))
from scipy.stats import mode
#计算众数
print(mode(data))

from numpy import mean, ptp, var, std

#极差
print(ptp(data))
#方差
print(var(data))
#标准差
print(std(data))
#变异系数
print(mean(data) / std(data))

from numpy import mean, std
#计算第一个值的z-分数
print((data[0]-mean(data)) / std(data))


from numpy import array, cov, corrcoef
data1=[1,2,3]
data2=[1,2,3]
data = array([data1, data2])

#计算两组数的协方差
#参数bias=1表示结果需要除以N，否则只计算了分子部分
#返回结果为矩阵，第i行第j列的数据表示第i组数与第j组数的协方差。对角线为方差
print(cov(data, bias=1))

#计算两组数的相关系数
#返回结果为矩阵，第i行第j列的数据表示第i组数与第j组数的相关系数。对角线为1
print(corrcoef(data))

import pandas as pd
df = pd.read_csv('datas.csv')
print(df['身高'])
print('均值',df['身高'].mean())
print('中位数', df['身高'].median())

print('方差', df['身高'].var())
print('标准差', df['身高'].std())
print('极差', df['身高'].max()-df['身高'].min())

print('偏度', df['身高'].skew())
print('峰度', df['身高'].kurt())


import numpy as np
import stats as sts
scores = [1,2,2,2,5]
#集中趋势的度量
print('求和：',np.sum(scores))
print('个数：',len(scores))
print('平均值:',np.mean(scores))
print('中位数:',np.median(scores))
print('众数:',sts.mode(scores))
print('上四分位数',sts.quantile(scores,p=0.25))
print('下四分位数',sts.quantile(scores,p=0.75))
#离散趋势的度量
print('最大值:',np.max(scores))
print('最小值:',np.min(scores))
print('极差:',np.max(scores)-np.min(scores))
print('四分位差',sts.quantile(scores,p=0.75)-sts.quantile(scores,p=0.25))
print('标准差:',np.std(scores))
print('方差:',np.var(scores))
print('离散系数:',np.std(scores)/np.mean(scores))
#偏度与峰度的度量
print('偏度:',sts.skewness(scores))
print('峰度:',sts.kurtosis(scores))


