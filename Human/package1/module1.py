import math
print(math.pi,math.e) #注意+和，的区别

a=100
A=100
print ('a+A='+str(a+A))
#多个变量赋值：
a,b,c=100,200,'Hello, world!'
print(a,c)

s='This is an example for Python programming'
print (s.split())

name=['David Nickson','Morgan Wang','John F. Kenedey','Jun Zhang']
print(name[0:4]) #注意list中;的使用规则
a=[1,2,['a','b']]
b=a
c=a[:]
a.append(3)
print(len(a))

age = 3
if age >= 18:
    print ('adult')
elif age >= 13:
    print ('teenager')
else:
    print ('kid')

s=0
for i in range(1,101):
    s+=i
    print (s)
d={'name':'David Nickson','age':76,'gender':'male','department':'Statistics'}
for key in d:
    print (key,d[key])

seq=[1,2,3,4,5]
for i in range(len(seq)):
    print (seq[i])

for a in 'This is Python!':
    if a==' ':
        pass
        print ('passed!')
        break
    print (a)

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

a=fact(5)
print(a)

def fab(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1

for n in fab(10):
      print (n)

def make_change(amount,coins=[1,5,10,25],hand=None):
    hand=[] if hand is None else hand
    if amount==0:
        yield hand
    for coin in coins:
        if coin>amount or (len(hand)>0 and hand[-1]<coin):
            continue
        for result in make_change(amount-coin,coins=coins,hand=hand+[coin]):
            yield result

for way in make_change(100,coins=[10,25,50]):
    print (way)
