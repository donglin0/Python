import numpy as np
import stats as sts
data = [1,2,2,3]
#集中趋势的度量
print('求和：',np.sum(data))
print('个数：',len(data))
print('平均值:',np.mean(data))
print('中位数:',np.median(data))
print('众数:',sts.mode(data))
print('上四分位数',sts.quantile(data,p=0.25))
print('下四分位数',sts.quantile(data,p=0.75))
#离散趋势的度量
print('最大值:',np.max(data))
print('最小值:',np.min(data))
print('极差:',np.max(data)-np.min(data))
print('四分位差',sts.quantile(data,p=0.75)-sts.quantile(data,p=0.25))
print('标准差:',np.std(data))
print('方差:',np.var(data))
print('变异系数:',np.std(data)/np.mean(data))
#偏度与峰度的度量
print('偏度:',sts.skewness(data))
print('峰度:',sts.kurtosis(data))




# 随机生成两个样本
x = np.random.randint(0, 9, 1000)
y = np.random.randint(0, 9, 1000)

# 计算平均值
mx = x.mean()
my = y.mean()

# 计算标准差
stdx = x.std()
stdy = y.std()

# 计算协方差矩阵
covxy = np.cov(x, y)
print(covxy)

# 我们可以手动进行验证
# covx等于covxy[0, 0], covy等于covxy[1, 1]

covx = np.mean((x - x.mean()) ** 2) 
covy = np.mean((y - y.mean()) ** 2) 
print(covx)
print(covy)
# 这里计算的covxy等于上面的covxy[0, 1]和covxy[1, 0]，三者相等
covxy = np.mean((x - x.mean()) * (y - y.mean()))
print(covxy)

# 下面计算的是相关系数矩阵(和上面的协方差矩阵是类似的)
coefxy = np.corrcoef(x, y)
print(coefxy)

