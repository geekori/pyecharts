'''

柱状图

'''
from pyecharts import Bar

attr = ['手机','电脑','汽车','书','鞋']
v1 = [30,23,54,22,53]
v2 = [34,45,23,45,12]

bar = Bar('柱状图演示')

bar.add('商家A',attr,v1,is_stack=False,mark_point=['average'])
bar.add('商家B',attr,v2,is_stack=False,mark_line=['min','max'])

bar.render('bar.html')
