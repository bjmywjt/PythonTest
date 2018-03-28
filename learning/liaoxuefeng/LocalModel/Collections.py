from collections import namedtuple


# namedtuple 应用
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(3, -2)
print('p1点坐标x:%s,y:%s' % p1)
print('p2点坐标x:%s,y:%s' % p2)

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(2, 2, 2)
print('c圆心坐标:(%s,%s) 半径:%s' % c)

# 
