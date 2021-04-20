import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
import math
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
def get_distance_from_point_to_line(point, line_point1, line_point2):
    #对于两点坐标为同一点时,返回点与点的距离
    if line_point1 == line_point2:
        point_array = np.array(point )
        point1_array = np.array(line_point1)
        return np.linalg.norm(point_array -point1_array )
    #计算直线的三个参数
    A = line_point2[1] - line_point1[1]
    B = line_point1[0] - line_point2[0]
    C = (line_point1[1] - line_point2[1]) * line_point1[0] + \
        (line_point2[0] - line_point1[0]) * line_point1[1]
    #根据点到直线的距离公式计算距离
    distance = np.abs(A * point[0] + B * point[1] + C) / (np.sqrt(A**2 + B**2))
    return distance

def qianjin_x(x):
    x_next = x + 0.5*math.cos(0.5194235)
    return x_next
def qianjin_y(y):
    y_next = y + 0.5*math.sin(0.5194235)
    return y_next
def point2point(x_1,y_1,x_2,y_2):
    p2pdis = math.sqrt((x_1-x_2)**2+(y_1-y_2)**2)
    return  p2pdis
def zhongdian(x1_p,y1_p,x2_p,y2_p):
    res_px = (x1_p+x2_p)/2
    res_py = (y1_p+y2_p)/2
    return res_px,res_py

def houtui_x(x):
    x_next = x - 0.5*math.cos(0.5194235)
    return x_next
def houtui_y(y):
    y_next = y - 0.5*math.sin(0.5194235)
    return y_next
# print(zhongdian(1,10,2,5))

def jugg(a,b,point1_x,point1_y,point2_x,point2_y,point3_x,point3_y,point4_x,point4_y):
    m = 0 ;n = 0
    if get_distance_from_point_to_line((a,b),(point1_x,point1_y), (point2_x,point2_y))>1.3 :
        m = 1
        if get_distance_from_point_to_line((a,b),(point3_x,point3_y), (point4_x,point4_y))>1.3:
            n=1
    return m*n
distance_zhangai = point2point(15.301006,10.696528,14.405506,11.953528)
R=np.sqrt((1.3+1+distance_zhangai/2)**2+2.5**2)+0.3
def isnotdaoche(x1,y1,x2,y2):
    if get_distance_from_point_to_line(zhongdian(14.405506, 11.953528, 15.301006, 10.696528),
                                            (x1, y1), (x2, y2)) <= R:
        print("需要倒车")
    else:
        print("不需要倒车就能调头")

#交点坐标
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
class Point(object):
    x = 0
    y = 0

    # 定义构造方法
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line(object):
    # a=0
    # b=0
    # c=0
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def GetLinePara(line):
    line.a = line.p1.y - line.p2.y;
    line.b = line.p2.x - line.p1.x;
    line.c = line.p1.x * line.p2.y - line.p2.x * line.p1.y;


def GetCrossPoint(l1, l2):
    GetLinePara(l1);
    GetLinePara(l2);
    d = l1.a * l2.b - l2.a * l1.b
    p = Point()
    p.x = (l1.b * l2.c - l2.b * l1.c) * 1.0 / d
    p.y = (l1.c * l2.a - l2.c * l1.a) * 1.0 / d
    return p;


def py_x(b):
    x_next = b + 4 * math.cos(0.5194235)
    return x_next
def py_y(a):
    y_next = a + 4 * math.sin(0.5194235)
    return y_next



