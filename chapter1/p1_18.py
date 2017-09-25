#!/usr/bin/env python3
# -*- coding:utf8 -*-
###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)

SHARES = slice(20,23)
PRICE = slice(31,37)

cost2 = int(record[SHARES])*float(record[PRICE])
print(cost2)

# slice(start,stop,step)
# list[start:stop:step]
a = slice(5,50,2)
print(a.start)
print(a.stop)
print(a.step)
print(a)

# 让切片参数小于等于可取的最大值
s = 'Helloworld'
a = a.indices(len(s))
print(a)