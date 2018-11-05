'''

梯形图和面积图

'''

from pyecharts import Line

attr = ['手机','电脑','汽车','书','鞋']
v1 = [30,23,54,22,53]
v2 = [34,45,23,45,12]

line = Line('折线图')
line.add('商家A',attr,v1,mark_point=["max"],is_step=True)
line.add('商家B',attr,v2,is_smooth=True,mark_line=["average"],is_fill=True,area_color='#F00',area_opacity=0.3)

line.render("line2.html")