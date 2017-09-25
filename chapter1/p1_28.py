#!/usr/bin/env python3
# -*- coding:utf8 -*-

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

from collections import ChainMap

# 如果有重复键，它会采用所出现的第一个映射中所对应的值
c = ChainMap(a,b)
print(c)
print('c[x]:',c['x'])
print('c[y]:',c['y'])
print('c[z]:',c['z'])

print(len(c))
print(list(c.keys()))
print(list(c.values()))

print('*'*40)

c['z'] = 10
c['w'] = 40
print(c)
#del c['y']
"""
Traceback (most recent call last):
  File "D:\Program Files\Python35\lib\collections\__init__.py", line 932, in __delitem__
    del self.maps[0][key]
KeyError: 'y'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "f:\Projects\2017\PythonCookbook\chapter1\p1_28.py", line 23, in <module>
    del c['y']
  File "D:\Program Files\Python35\lib\collections\__init__.py", line 934, in __delitem__
    raise KeyError('Key not found in the first mapping: {!r}'.format(key))
KeyError: "Key not found in the first mapping: 'y'"
"""
print('*'*40)

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3

print(values)
print("values['x'] =",values['x'])

values = values.parents
print(values)
print("values['x'] =",values['x'])

values = values.parents
print(values)
print("values['x'] =",values['x'])

print('*'*40)

merged = dict(b)
merged.update(a)
print("merged['x'] =",merged['x'])
print("merged['y'] =",merged['y'])
print("merged['z'] =",merged['z'])

print('*'*40)

merged = ChainMap(a, b)
print("merged['x'] =",merged['x'])
a['x'] = 9
print("merged['x'] =",merged['x'])