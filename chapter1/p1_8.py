#!/usr/bin/env python3
# -*- coding:utf8 -*-

from collections import deque

# deque 应用实例

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print('q:',q)

q.append(4)
print('q:',q)

q.append(5)
print('q:',q)

# 不设定大小时deque大小无限，可以在前后插入
q2 = deque()
q2.append(1)
q2.append(2)
q2.append(3)
print('q2:',q2)

q2.appendleft(4)
print('q2:',q2)