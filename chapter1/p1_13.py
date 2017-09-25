#!/usr/bin/env python3
# -*- coding:utf8 -*-

from collections import OrderedDict
import json

# 顺序字典
# 它通过两个链表来实现的，所以它所消耗的内存大小是原始字典的两倍
def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])
    print(json.dumps(d))

ordered_dict()

"""
foo 1
bar 2
spam 3
grok 4
{"foo": 1, "bar": 2, "spam": 3, "grok": 4}
"""