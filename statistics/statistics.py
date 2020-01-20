#导入模块（module）
import numpy as np
import stats as sts
#声明类
class statistic(object):
    #构造函数
    def __init__(self):
        pass
    #集中趋势的度量
    def len(self,data):
        print('个数：',len(data))
    def sum(self,data):
        print('求和：',np.sum(data))
    def mean(self,data):
        print('平均值:',np.mean(data))
    def median(self,data):
        print('中位数:',np.median(data))
    def mode(self,data):
        print('众数:',sts.mode(data))
    def quantile1(self,data):
        print('上四分位数:',sts.quantile(data,p=0.25))
    def quantile2(self,data):
        print('下四分位数:',sts.quantile(data,p=0.75))
    #离散趋势的度量
    def max(self,data):
        print('最大值:',np.max(data))
    def min(self,data):
        print('最小值:',np.min(data))
    def range(self,data):
        print('极差:',np.max(data)-np.min(data))
    def interquartile_range(self,data):
        print('四分位差:',sts.quantile(data,p=0.75)-sts.quantile(data,p=0.25))
    def std(self,data):
        print('标准差:',np.std(data))
    def var(self,data):
        print('方差:',np.var(data))
    def cov(self,data1,data2):
        print('协方差矩阵:\n', np.cov(data1, data2))
    def corrcoef(self,data1,data2):
        print('相关系数矩阵:\n', np.corrcoef(data1, data2))
    def coefficient_of_variation(self,data):
        print('变异系数:',np.std(data)/np.mean(data))
    #偏度与峰度的度量
    def skewness(self,data):
        print('偏度:',sts.skewness(data))
    def kurtosis(self,data):
        print('峰度:',sts.kurtosis(data))

#使用类
data=[1,2,2,3]#测试数据
st=statistic()#类实例化
st.len(data)#数据个数
st.sum(data)#求和
st.mean(data)#平均数
st.median(data)#中位数
st.mode(data)#众数
st.quantile1(data)#上四分位数
st.quantile2(data)#下四分位数

st.max(data)#最大值
st.min(data)#最小值
st.range(data)#极差
st.interquartile_range(data)#四分位差
st.std(data)#标准差
st.var(data)#方差
st.coefficient_of_variation(data)#变异系数

st.skewness(data)#偏度
st.kurtosis(data)#峰度

data1=[1,2,3,4]#计算协方差和相关系数的两组数据
data2=[2,4,6,8]
st.cov(data1,data2)#协方差矩阵
st.corrcoef(data1,data2)#相关系数矩阵



