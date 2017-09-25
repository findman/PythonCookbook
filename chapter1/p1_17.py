#!/usr/bin/env python3
# -*- coding:utf8 -*-

def dedupe(items, key=None):
    seen = set()
    print('key:',key)
    for item in items:
        # 如果key为空返回item；如果非空则返回匿名函数所返回的值
        val = item if key is None else key(item)
        print('val:',val)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x':1, 'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]

# 这里的本质是通过匿名函数取到字典的数据，并放入set，然后再进行比较
l = list(dedupe(a,key=lambda d:(d['x'],d['y'])))
l2 = list(dedupe(a,key=lambda d:d['x']))
l3 = list(dedupe(a,key=lambda d:d['y']))


print(l)
print(l2)
print(l3)

"""
[{'y': 2, 'x': 1}, {'y': 3, 'x': 1}, {'y': 4, 'x': 2}]
[{'y': 2, 'x': 1}, {'y': 4, 'x': 2}]
[{'y': 2, 'x': 1}, {'y': 3, 'x': 1}, {'y': 4, 'x': 2}]
"""
