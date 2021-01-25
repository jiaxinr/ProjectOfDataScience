#对更细致的走势进行分析计算并绘图

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
l=[[],[],[],[],[]]
lab=['关注关切','担忧焦虑','期盼希望','不满无语','理性','祝福支持','感动感谢','关注国外','乐观快乐']
dict = {'关注关切': 1, '担忧焦虑': 2, '期盼希望': 3,'不满无语': 4, '理性': 5, '祝福支持': 6,'感动感谢': 7, '关注国外': 8, '乐观快乐': 9}
name=['1.26-1.31','2.1-2.10','2.10-2.15','2.15-2.29','时间段不详']

a=[[],[],[],[],[]]
for i in range(0,5):
    path=name[i]+'.txt'
    with open(path,encoding='utf8') as f:
        num=f.read().split()
        print(num)
        for j in range(0,108,13):
            l[i].append(num[j])
        for j in range(12,120,13):
            a[i].append(num[j])
print(l)
x=[1,2,3,4,5]
num=[]
for i in range(0,9):
    num.append([0.0]*5)

for i in range(0,5):
    tot=0
    for j in range(0,9):
        tot+=float(a[i][j])
    for j in range(0,9):
        p=dict[l[i][j]]
        #print(p)
        num[j][i]=float(a[i][p-1])/tot
for i in range(0,9):
    plt.plot(x, num[i], marker='*', ms=10, label=lab[i], data=None)
# plt.plot(x, numa, marker='*', ms=10, label="积极",data=None)
# plt.plot(x, numb, marker='*', ms=10, label="消极",data=None)
# plt.plot(x, numc, marker='*', ms=10, label="中立",data=None)
#
# plt.xticks(rotation=45)
#
#
#
plt.xlabel("疫情发展阶段阶段")
plt.ylabel("TF-IDF占比*10")
plt.title("不同阶段情绪占比发展")
plt.legend(loc="upper left")
# # 在折线图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
# for y in [numa,numb,numc]:
#     for x1, yy in zip(x, y):
#         pass
#         #plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=20, rotation=0)
plt.savefig("a.jpg")
plt.show()
