#!/usr/bin/env python3
# -*- coding:utf8 -*-

p = (4, 5)
x, y = p
print("x:", x)
print("y:", y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print("name = %s, shares = %d, price = %f, date = %s" % (name, shares, price, str(date)))

name , shares, price, (year, mon, day) = data
print("name = %s, shares = %d, price = %f, year = %d, mon = %d, day = %d" % (name, shares, price, year, mon, day))

# 错误示例
"""
错误信息：
Traceback (most recent call last):
  File "x:\PythonCookbook\chapter1\p1_1.py", line 17, in <module>
    name , shares = data
ValueError: too many values to unpack (expected 2)
"""
# name , shares = data
