#横坐标就为数量，纵坐标为对应数量的样本个数

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义目标函数
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# 这部分生成样本点，对函数值加上高斯噪声作为样本点
# [0, 4]共50个点
x = []
y = [0]*10
for i in range(1,11):
    x.append(i)
with open ("bilibili.txt",encoding="utf8") as f:
    a=f.read().split()
print(a)
# with open ("dataofRMRB.txt",encoding="utf8") as f:
#     a=f.readline()
#     while a!="":
#         print(a)
#         if(a=='\n'):
#             continue
#         c=int(int(a)/1000)
#         if(c>9):
#             c=9
#         y[c]=y[c]+1
#         a=f.readline()
#print(xdata)

# a=2.5, b=1.3, c=0.5
for i in range(0,len(a)):
    c = int(int(a[i]) / 100000)
    print(c)
    if(c>9):
        c=9
    y[c]=y[c]+1
print(x)
print(y)
xdata=np.array(x)
ydata=np.array(y)


# 生成均值为0，标准差为err_stdev为0.2的高斯噪声
plt.figure('拟合图')
plt.plot(xdata, ydata, 'b-', label='data')


# 利用curve_fit作简单的拟合，popt为拟合得到的参数,pcov是参数的协方差矩阵
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


# 限定参数范围：0<=a<=3, 0<=b<=1, 0<=c<=0.5
#popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata, func(xdata, *popt), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()