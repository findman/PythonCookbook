#!/usr/bin/env python3
# -*- coding:utf8 -*-

s = 'Hello'
a, b, c, d, e = s
print("a = %s, b = %s, c = %s, d = %s, e = %s" % (a, b, c, d, e))

# 使用占位符实现获取部分数据
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print("shares = %d" % shares)
print("price = %f" % price)