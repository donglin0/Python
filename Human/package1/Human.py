class Human(object):  #这才是注释，有点奇妙哦
    domain='eukarya' #类属性
    #构造函数,便于给实例的对象传递参数
    def __init__(self,kingdom='Animalia',phylum='Chordata',order='Primates',family='Human Being'):
        self.kingdom=kingdom #实例属性
        self.phylum=phylum
        self.order=order
        self.family=family
    def typewrite(self):
        print ('This is %s typing words!' %self.family)
    def add(self,n1,n2):
        n=n1+n2
        print ( str(n1) + '+' +str(n2) + '=' + str(n))
        print ('You see! %s can calculate!' %self.family)
    @classmethod
    def showclassmethodinfo(cls):
        print (cls.__name__) #__name__属性，其值为类名
        print (dir(cls)) #使⽤dir列示本类的所有⽅法
    @staticmethod #装饰器
    def showclassattributeinfo():
        print (Human.__dict__) #__dict__属性，返回⼀个键为属性名、键值为属性值的字典

#数据输入输出
#inp=input("Please enter your input:")
#print(inp)

#文件的读取写入
path='test.txt'
fp=open(path,'a')
fp.write('--donglin0') #写入文件中
print(fp.mode,fp.name)
fp.close()

fp=open(path,'r')
print(fp.readlines()) #从文件中读取
print(fp.tell())
fp.close()

#导入模块（module）
import os
print(os.getcwd()) #显示文件路径

import math
print(math.floor(99.9))
quzheng=math.floor
print(quzheng(99.9))
from math import sqrt
print(sqrt(100))

