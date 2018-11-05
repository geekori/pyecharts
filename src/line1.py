'''

折线图

'''

from pyecharts import Line

attr = ['手机','电脑','汽车','书','鞋']
v1 = [30,23,54,22,53]
v2 = [34,45,23,45,12]

line = Line('折线图')
line.add('商家A',attr,v1,mark_point=["max"])
line.add('商家B',attr,v2,is_smooth=True,mark_line=["average"])

line.render("line1.html")