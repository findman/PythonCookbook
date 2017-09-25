#!/usr/bin/env python3
# -*- coding:utf8 -*-
from collections import namedtuple
Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('jonsey@example.com','2012-10-19')

print(sub)

print(sub.addr)
print(sub.joined)
print(len(sub))

addr, joined = sub
print(addr)
print(joined)

print('*'*40)

Stock = namedtuple('Stock',['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

records = [
    ('x', 4, 2),
    ('y', 9, 4)
]

print(compute_cost(records))

print('*'*40)

s = Stock('ACME', 100, 123.45)
print(s)
# 数据只读
#s.shares = 75

# 替换并返回一个新对象
s = s._replace(shares = 75)
print(s)

