import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
import math
import func
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
import pandas as pd
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import math
# h=math.atan(0.6080070686637377)
# print(h)
import numpy as np


a=6.53023;b=3.970426


# distance=get_distance_from_point_to_line((6.53023,3.970426), (1.380606,2.756528), (15.301006,10.696528))
distance=func.get_distance_from_point_to_line((5,12), (0,26), (20,15))
print(func.point2point(2,3,4,5))
print(distance)
fig = plt.figure()



# # ax = fig.add_subplot(211, aspect='auto')
# fig,ax=plt.subplots()
plt.plot((1.380606,15.301006,14.405506,0.134806),(2.756528,10.696528,11.953528,3.744528))
#求障碍物顶点到轨迹线距离
distance2 = func.get_distance_from_point_to_line((15.301006,10.696528),(a,b),(func.qianjin_x(a),func.qianjin_y(b)))
print(distance2)
distance_zhangai=func.point2point(15.301006,10.696528,14.405506,11.953528)
print("障碍物宽度")
print(distance_zhangai)
# ax = fig.add_subplot(111)   #创建子图
# x=(6.53023)
# y=(3.970426)
# rect = plt.Rectangle((0.1,0.2),0.4,0.3, fill=False,edgecolor="red")    # （0.1，0.2）为左下角的坐标，0.4，0.3为宽和高，负数为反方向，红色填充
# plt.scatter(x,y)
# x,y=qianjin(x,y)
# plt.scatter(x,y)
a=6.53023;b=3.970426
# plt.scatter(a, b,s = 35, marker='*', c ='g')

hengzuobiao=[]
zongzuobiao=[]
while(func.jugg(func.qianjin_x(a),func.qianjin_y(b),1.380606,2.756528, 15.301006,10.696528,2.998806,0.220528, 30.323206,15.844528)==1):
    plt.plot((1.380606, 15.301006, 14.405506, 0.134806,1.380606), (2.756528, 10.696528, 11.953528, 3.744528,2.756528),c ='r')
    plt.plot((2.998806,30.323206,23.792806,-4.748594,2.998806), (0.220528,15.844528,29.414528,12.996528,0.220528),c='b')
    plt.plot((11.149906,-3.120794), (18.121528,9.912528),c='#EE7621')
    plt.plot((12.777706,-1.492994), (15.037528,6.828528),c='g')
    plt.plot((6.783106,2.529706,5.012206,9.265606,6.783106),
             (19.744528,17.311528,12.971528,15.404528,19.744528), c='#8B4513')
    a=func.qianjin_x(a)
    b=func.qianjin_y(b)
    hengzuobiao.append(a)
    zongzuobiao.append(b)
    plt.xlim(-5, 30)
    plt.ylim(0, 30)
    plt.plot(hengzuobiao, zongzuobiao,'+',c ='#1C1C1C')
    plt.show()
    # plt.close('all')
    if func.point2point(15.301006,10.696528,func.qianjin_x(a),func.qianjin_y(b)) - func.point2point(15.301006,10.696528,a,b) > 0 :
        break
print("直行停止点")
print(a,b)
r = distance_zhangai/2+distance2
print("最小转弯半径")
print(r)
print(hengzuobiao)
yuandian_x,yuandian_y = func.zhongdian(14.405506,11.953528,15.301006,10.696528)
print("圆心")
print(yuandian_x,yuandian_y)
print("最大转弯半径")
max_dis= func.get_distance_from_point_to_line((a,b),(5.012206,12.971528),(9.265606,15.404528))
max_r = (max_dis-1.3)/2
print(max_r)
# half = Wedge(yuandian_x,yuandian_y,r,0.5194235*(180/3014159),180)
# ax.add_patch(half)
# # 设置xy轴等长，否则不圆
# plt.axis('equal')
# plt.show()
print("开始转弯")
circle_x = a
while(circle_x < yuandian_x+r):
    # circle_x = 10
    circle_y = -1*abs(np.sqrt(abs(r**2-np.power((circle_x-yuandian_x),2))))+ yuandian_y
    plt.plot((1.380606, 15.301006, 14.405506, 0.134806,1.380606), (2.756528, 10.696528, 11.953528, 3.744528,2.756528),c ='r')
    plt.plot((2.998806,30.323206,23.792806,-4.748594,2.998806), (0.220528,15.844528,29.414528,12.996528,0.220528),c='b')
    plt.plot((11.149906,-3.120794), (18.121528,9.912528),c='#EE7621')
    plt.plot((12.777706,-1.492994), (15.037528,6.828528),c='g')
    plt.plot((6.783106, 2.529706, 5.012206, 9.265606, 6.783106),
             (19.744528, 17.311528, 12.971528, 15.404528, 19.744528), c='#8B4513')
    hengzuobiao.append(circle_x)
    zongzuobiao.append(circle_y)
    circle_x = circle_x + 0.25
    plt.xlim(-5, 30)
    plt.ylim(0, 30)
    plt.plot(hengzuobiao, zongzuobiao,'+',c ='#1C1C1C')
    plt.show()


circle_x = yuandian_x+r
while(circle_x > yuandian_x-(r*math.sin(0.5194235))):
    # circle_x = 10
    circle_y = abs(np.sqrt(abs(r**2-np.power((circle_x-yuandian_x),2))))+ yuandian_y
    plt.plot((1.380606, 15.301006, 14.405506, 0.134806,1.380606), (2.756528, 10.696528, 11.953528, 3.744528,2.756528),c ='r')
    plt.plot((2.998806,30.323206,23.792806,-4.748594,2.998806), (0.220528,15.844528,29.414528,12.996528,0.220528),c='b')
    plt.plot((11.149906,-3.120794), (18.121528,9.912528),c='#EE7621')
    plt.plot((12.777706,-1.492994), (15.037528,6.828528),c='g')
    plt.plot((6.783106, 2.529706, 5.012206, 9.265606, 6.783106),
             (19.744528, 17.311528, 12.971528, 15.404528, 19.744528), c='#8B4513')
    hengzuobiao.append(circle_x)
    zongzuobiao.append(circle_y)
    plt.xlim(-5, 30)
    plt.ylim(0, 30)
    plt.plot(hengzuobiao, zongzuobiao,'+',c ='#1C1C1C')
    plt.show()
    circle_x = circle_x - 0.25
print("转弯结束点")
print(circle_x,circle_y)
a = circle_x;b = circle_y
print("开始直行")
# print(jugg(houtui_x(a),houtui_y(b),14.405506,11.953528,0.134806,3.744528,12.777706,15.037528,-1.492994,6.828528))
while(func.jugg(func.houtui_x(a),func.houtui_y(b),14.405506,11.953528,0.134806,3.744528,12.777706,15.037528,-1.492994,6.828528)==1):
    plt.plot((1.380606, 15.301006, 14.405506, 0.134806,1.380606), (2.756528, 10.696528, 11.953528, 3.744528,2.756528),c ='r')
    plt.plot((2.998806,30.323206,23.792806,-4.748594,2.998806), (0.220528,15.844528,29.414528,12.996528,0.220528),c='b')
    plt.plot((11.149906,-3.120794), (18.121528,9.912528),c='#EE7621')
    plt.plot((12.777706,-1.492994), (15.037528,6.828528),c='g')
    plt.plot((6.783106, 2.529706, 5.012206, 9.265606, 6.783106),
             (19.744528, 17.311528, 12.971528, 15.404528, 19.744528), c='#8B4513')
    a=func.houtui_x(a)
    b=func.houtui_y(b)
    hengzuobiao.append(a)
    zongzuobiao.append(b)
    plt.xlim(-5, 30)
    plt.ylim(0, 30)
    plt.plot(hengzuobiao, zongzuobiao,'+',c ='#1C1C1C')
    plt.show()
    print("一次")
    if func.get_distance_from_point_to_line((a,b),(2.998806,0.220528),(-4.748594,12.996528)) < 2.8 :
        break
print("马上撞墙")
print("最终坐标,停车")
print(a,b)
print("路径坐标")
print(hengzuobiao)
print(zongzuobiao)
# for i in range(len(hengzuobiao)):
#     plt.plot((1.380606, 15.301006, 14.405506, 0.134806, 1.380606), (2.756528, 10.696528, 11.953528, 3.744528, 2.756528),
#              c='r')
#     plt.plot((2.998806, 30.323206, 23.792806, -4.748594, 2.998806),
#              (0.220528, 15.844528, 29.414528, 12.996528, 0.220528), c='b')
#     plt.plot((11.149906, -3.120794), (18.121528, 9.912528), c='#EE7621')
#     plt.plot((12.777706, -1.492994), (15.037528, 6.828528), c='g')
#     plt.xlim(-5, 30)
#     plt.ylim(0, 30)
#     plt.plot(hengzuobiao[i], zongzuobiao[i], '+', c='#1C1C1C')
#     plt.show()




# x1 = np.random.normal(2,1.2,300)
# print(x1)
# ax.add_patch(rect)
# plt.scatter(hengzuobiao, zongzuobiao,s=35,marker='*', c ='g')
# plt.show()