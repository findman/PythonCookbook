#!/usr/bin/env python3
# -*- coding:utf8 -*-

prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

# zip反转key和value，然后返回zip对象
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(),prices.keys()))

print('min_price:', min_price)
print('max_price:', max_price)

# 从输出可以看到zip实际是将字典转换为了元组
# 同时它是一个只能访问一次的迭代器
p = zip(prices.values(), prices.keys())
print(p)
for k in p:
    print(type(k))
    print(k)

"""
<class 'tuple'>
(205.55, 'IBM')
<class 'tuple'>
(10.75, 'FB')
<class 'tuple'>
(612.78, 'AAPL')
<class 'tuple'>
(37.2, 'HPQ')
<class 'tuple'>
(45.23, 'ACME')
"""