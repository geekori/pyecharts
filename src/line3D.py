'''

绘制3D曲线图

'''


from pyecharts import Line3D

import math

data = []
for t in range(0,30000):
    _t = t/1000
    x = (1 + 0.3 * math.cos(80*_t)) * math.cos(_t)
    y = (1 + 0.3 * math.cos(80 * _t)) * math.sin(_t)
    z = _t + 2.0 * math.sin(75*_t)
    data.append([x,y,z])

range_colors = ['#323799','#457745','#7543ad','#e0f3f8','#ffffbf','#fee091','#fdda66','#d73028']
line3d = Line3D('3D折线',width = 1200,height = 600)
line3d.add("",data,is_visualmap=True,visual_range_color=range_colors,visual_range=[0,30],grid3d_rotate_sensitivity=2)
line3d.render('line3d.html')


