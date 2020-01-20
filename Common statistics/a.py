#-*-coding:utf-8
import time;
import random;
class Math:
    #求极差
    @staticmethod
    def range(l):
        return max(l)-min(l);
    #求平均数
    @staticmethod
    def avg(l):
        return float(sum(l))/len(l);
    #求中位数
    @staticmethod
    def median(l):
        l=sorted(l);#先排序
        if len(l)%2==1:
            return l[len(l)/2];
        else:
            return (l[len(l)/2-1]+l[len(l)/2])/2.0;
    #求众数
    @staticmethod
    def mode(l):
        #统计list中各个数值出现的次数
        count_dict={};
        for i in l:
            if count_dict.has_key(i):
                count_dict[i]+=1;
            else:
                count_dict[i]=1;
        #求出现次数的最大值
        max_appear=0
        for v in count_dict.values():
            if v>max_appear:
                max_appear=v;
        if max_appear==1:
            return;
        mode_list=[];
        for k,v in count_dict.items():
            if v==max_appear:
                mode_list.append(k);
        return mode_list;
    #求方差
    @staticmethod
    def variance(l):#平方的期望-期望的平方
        s1=0;
        s2=0;
        for i in l:
            s1+=i**2;
            s2+=i;
        return float(s1)/len(l)-(float(s2)/len(l))**2;
    
    #求方差2
    @staticmethod    
    def variance2(l):#平方-期望的平方的期望
        ex=float(sum(l))/len(l);
        s=0;
        for i in l:
            s+=(i-ex)**2;
        return float(s)/len(l);    
 
