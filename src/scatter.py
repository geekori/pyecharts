'''

散点图

add

'''

from pyecharts import Scatter

x1 = [20, 13, 43, 53,34,89]
y1 = [10, 32, 43, 13, 54, 87]

x2 = [12, 24, 41, 33,54,19]
y2 = [13, 39, 31, 43, 24, 37]
scatter = Scatter('散点图')
scatter.add('A',x1,y1)
scatter.add('B',x2,y2,is_visualmap=True,visual_type='size',visual_range_size=[10,80])
scatter.render('a.html')


