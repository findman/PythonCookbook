#!/usr/bin/env python3
# -*- coding:utf8 -*-
# 仅支持可哈希对象
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]

# for k in dedupe(a):
#     print(k)
l = list(dedupe(a))
print(l)