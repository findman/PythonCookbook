#!/usr/bin/env python3
# -*- coding:utf8 -*-

from collections import defaultdict

d ={}
pairs = [('a',2),('b',3),('c',4)]

# for key,value in pairs:
#     # 如果不存在则创建key
#     if key not in d:
#         d[key] = []
#     d[key].append(value)

# 这里利用了defaultdict自动创建不存在的key
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

print(d)