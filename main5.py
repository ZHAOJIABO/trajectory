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
    plt.plot((func.py_x(20.072206),func.py_x(13.127906),func.py_x(14.071306),func.py_x(21.015606),func.py_x(20.072206)), (func.py_y(18.822528),func.py_y(14.850528),func.py_y(13.201528),func.py_y(17.173528),func.py_y(18.822528)),
             c='#9A32CD')
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
print("直行停止点1")
print(a,b)
print("判断是否转弯")
#判断缝隙距离 1.29m
jianxi_dis=func.point2point(14.071306,13.201528,14.405506,11.953528)
if jianxi_dis<2.6:
    print("间隙距离为 %f ,不能掉头" %jianxi_dis)
    while (func.jugg(func.qianjin_x(a), func.qianjin_y(b), 1.380606, 2.756528, 15.301006, 10.696528, 2.998806, 0.220528,
                     30.323206, 15.844528) == 1):
        plt.plot((1.380606, 15.301006, 14.405506, 0.134806, 1.380606),
                 (2.756528, 10.696528, 11.953528, 3.744528, 2.756528), c='r')
        plt.plot((2.998806, 30.323206, 23.792806, -4.748594, 2.998806),
                 (0.220528, 15.844528, 29.414528, 12.996528, 0.220528), c='b')
        plt.plot((11.149906, -3.120794), (18.121528, 9.912528), c='#EE7621')
        plt.plot((12.777706, -1.492994), (15.037528, 6.828528), c='g')
        plt.plot((func.py_x(20.072206), func.py_x(13.127906), func.py_x(14.071306), func.py_x(21.015606),
                  func.py_x(20.072206)), (
                 func.py_y(18.822528), func.py_y(14.850528), func.py_y(13.201528), func.py_y(17.173528),
                 func.py_y(18.822528)),
                 c='#9A32CD')
        a = func.qianjin_x(a)
        b = func.qianjin_y(b)
        hengzuobiao.append(a)
        zongzuobiao.append(b)
        plt.xlim(-5, 30)
        plt.ylim(0, 30)
        plt.plot(hengzuobiao, zongzuobiao, '+', c='#1C1C1C')
        plt.show()
        # plt.close('all')
        if func.point2point(21.015606,17.173528, func.qianjin_x(a), func.qianjin_y(b)) - func.point2point(21.015606,17.173528, a,
                                                                                                           b) > 0:
            break
print("直行停止点2")
print(a,b)
a=func.py_x(a)
b = func.py_y(b)

distance2 = func.get_distance_from_point_to_line((a,b),(1.380606,2.756528),(15.301006,10.696528))
print(distance2)
distance_zhangai=func.get_distance_from_point_to_line((20.072206,18.822528),(1.380606,2.756528),(15.301006,10.696528))
print("障碍物宽度")
print(distance_zhangai)

r = distance_zhangai/2+distance2
print("转弯半径")
print(r)
#交点坐标
p1 = func.Point(1.380606,2.756528)
p2 = func.Point(15.301006,10.696528)
line1 = func.Line(p1, p2)

p3 = func.Point(20.072206,18.822528)
p4 = func.Point(21.015606,17.173528)
line2 = func.Line(p3, p4)
Pc = func.GetCrossPoint(line1, line2)
# print("Cross point:", Pc.x, Pc.y);
yuandian_x,yuandian_y = func.zhongdian(20.072206,18.822528,Pc.x, Pc.y)
print("圆心坐标")
print(yuandian_x,yuandian_y)
yuandian_x = func.py_x(yuandian_x)
yuandian_y = func.py_y(yuandian_y)
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
    plt.plot(
        (func.py_x(20.072206), func.py_x(13.127906), func.py_x(14.071306), func.py_x(21.015606), func.py_x(20.072206)),
        (func.py_y(18.822528), func.py_y(14.850528), func.py_y(13.201528), func.py_y(17.173528), func.py_y(18.822528)),
        c='#9A32CD')
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
    plt.plot(
        (func.py_x(20.072206), func.py_x(13.127906), func.py_x(14.071306), func.py_x(21.015606), func.py_x(20.072206)),
        (func.py_y(18.822528), func.py_y(14.850528), func.py_y(13.201528), func.py_y(17.173528), func.py_y(18.822528)),
        c='#9A32CD')
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
while(func.jugg(func.houtui_x(a),func.houtui_y(b),13.127906,14.850528,20.072206,18.822528,11.149906,18.121528,-3.120794,9.912528)==1):
    plt.plot((1.380606, 15.301006, 14.405506, 0.134806,1.380606), (2.756528, 10.696528, 11.953528, 3.744528,2.756528),c ='r')
    plt.plot((2.998806,30.323206,23.792806,-4.748594,2.998806), (0.220528,15.844528,29.414528,12.996528,0.220528),c='b')
    plt.plot((11.149906,-3.120794), (18.121528,9.912528),c='#EE7621')
    plt.plot((12.777706,-1.492994), (15.037528,6.828528),c='g')
    plt.plot(
        (func.py_x(20.072206), func.py_x(13.127906), func.py_x(14.071306), func.py_x(21.015606), func.py_x(20.072206)),
        (func.py_y(18.822528), func.py_y(14.850528), func.py_y(13.201528), func.py_y(17.173528), func.py_y(18.822528)),
        c='#9A32CD')
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