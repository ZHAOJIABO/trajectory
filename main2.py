import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
import func

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
distance_zhangai = func.point2point(15.301006,10.696528,14.405506,11.953528)
R=np.sqrt((1.3+1+distance_zhangai/2)**2+2.5**2)+0.3
print("请输入障碍物右侧边界上的任意两点的横纵坐标！")
val_1x=eval(input('第一个点的横坐标:'))
val_1y=eval(input('第一个点的纵坐标:'))
val_2x=eval(input('第二个点的横坐标:'))
val_2y=eval(input('第二个点的纵坐标:'))
func.isnotdaoche(val_1x,val_1y,val_2x,val_2y)

