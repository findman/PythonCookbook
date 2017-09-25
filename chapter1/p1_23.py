#!/usr/bin/env python3
# -*- coding:utf8 -*-

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
"""
列表推导式

    数据结果
       |      数据源
       |        |        数据筛选
       |        |           |
       = =============== ========
print([n for n in mylist if n > 0])
"""
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# 如果数据量大可改为生成器表达式，通过迭代生成结果
pos = (n for n in mylist if n > 0)
print(pos) #<generator object <genexpr> at 0x000002158F08D620>

for x in pos:
    print(x)

print('*'*40)

# 非标处理
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError as e:
        return False

ivals = list(filter(is_int,values))
print(ivals)

print('*'*40)
# 列表推导式数据处理
import math
"""
列表推导式数据转换

         数据转换
            |            数据源
            |              |        数据筛选
            |              |           |
       ============ =============== ========
print([math.sqrt(n) for n in mylist if n > 0])
"""
print([math.sqrt(n) for n in mylist if n > 0])

# 列表推导式完整应用
#
#        数据转换
#           |           数据替换
#           |              |             数据源
#           |              |               |         数据筛选
#           |              |               |            |
#      ============ =============== =============== =========
print([math.sqrt(n) if n > 0 else 0 for n in mylist if n > -7])


print('*'*40)

addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK'
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n>5 for n in counts]
print(more5)
# compress依据第二个参数筛选数据
l = list(compress(addresses,more5))
print(l)
