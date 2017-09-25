#!/usr/bin/env python3
# -*- coding:utf8 -*-

from collections import defaultdict

# 保留元素插入顺序
d = defaultdict(list)
d['a'].append(3)
d['a'].append(5)
d['b'].append(6)

# 去重
d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['b'].add(4)

print(d)
print(d2)