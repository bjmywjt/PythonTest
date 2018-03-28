from collections import namedtuple, deque, defaultdict, OrderedDict


# namedtuple 应用
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(3, -2)
print('p1点坐标x:%s,y:%s' % p1)
print('p2点坐标x:%s,y:%s' % p2)

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(2, 2, 2)
print('c圆心坐标:(%s,%s) 半径:%s' % c)

# deque 双向列表应用
dq = deque(['A', 'b', 'C'])
dq.append('D')
dq.appendleft('Z')
print(dq)


# defaultdict 应用
dd = defaultdict(lambda: 'N/A')
dd['k'] = 'wjt'
print(dd['k'])
print(dd['j'])

# OrderedDict 有序dict应用
d = dict([('A', 1), ('B', 2), ('C', 3)])
print(d)
od = OrderedDict([('A', 1), ('B', 2), ('C', 3)])
print(od)
