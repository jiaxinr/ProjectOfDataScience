#对于粗糙的情绪划分（即积极、消极、中立）分析计算绘图
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文

a=[]
b=[]
c=[]

a.append([580 ,0.31402273957769355 ,0.7829517994403864 ,0.18631215845978047])#积极
b.append([473 ,0.2560909583107742 ,1.0518389315196182 ,0.327675894826181])#消极
c.append([794 ,0.4298863021115322 ,0.507317356826959 ,0.4927857182707951])#中立


a.append([3057, 0.27289769683985005, 3.092749970485182, 0.25808824291963767])#积极
b.append([2456, 0.2192465631137297, 3.513672026015883, 0.36431602685823333])#消极
c.append([5689, 0.5078557400464203, 2.749448224805253, 0.6402417758331728])#中立


a.append([360, 0.33707865168539325, 0.5849625007211562, 0.26057516077221105])#积极
b.append([178,0.16666666666666666, 1.5849625007211563, 0.29953420647636586])#消极
c.append([530,0.49625468164794007,0.45193708209037303, 0.7766049386221198])#中立


a.append([1221, 0.35691318327974275, 3.8925595748990376, 1.3893058289832578])#积极
b.append([587, 0.17158725518854137, 4.948233172588196, 0.8490537481172965])#消极
c.append([1613, 0.47149956153171585, 4.018504251633916, 1.894722992658727])#中立


a.append([3789 ,0.38829678212748514, 1.0946699183790984, 0.3282702718423571])#积极
b.append([1383 ,0.14172986267677803, 2.221526197929525, 0.4196852894564608])#消极
c.append([4586 ,0.46997335519573685 ,1.067857087245132 ,0.6268470538070423])#中立


numa=[0]*5
numb=[0]*5
numc=[0]*5
for i in range(0,5):
    tot=a[i][3]+b[i][3]+c[i][3]
    numa[i] = a[i][3] / tot * 10
    numb[i] = b[i][3] / tot * 10
    numc[i] = c[i][3] / tot * 10
x = [1, 2, 3, 4,5]

plt.plot(x, numa, marker='*', ms=10, label="积极",data=None)
plt.plot(x, numb, marker='*', ms=10, label="消极",data=None)
plt.plot(x, numc, marker='*', ms=10, label="中立",data=None)

plt.xticks(rotation=45)



plt.xlabel("疫情发展阶段阶段")
plt.ylabel("TF-IDF占比*10")
plt.title("不同阶段情绪占比发展")
plt.legend(loc="upper left")
# 在折线图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for y in [numa,numb,numc]:
    for x1, yy in zip(x, y):
        pass
        #plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=20, rotation=0)
plt.savefig("a.jpg")
plt.show()
