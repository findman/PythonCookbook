#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:删除字符串中不需要的字符
Desc:
"""

import re

def strip_fun():
    s = ' hello world \n'
    # 移除所有空格回车
    print(s.strip())
    # 移除左边的
    print(s.lstrip())
    # 移除右边的
    print(s.rstrip())
    t = '-----hello====='
    # 移除左边特定字符
    print(t.lstrip('-'))
    # 移除多个字符
    print(t.strip('-='))
    # 测试字符
    t2 = '---===hello===---'
    print(t2.rstrip('-='))

    s = 'hello     world \n'
    s = s.strip()
    # 注意strip仅移除左右两侧的空格和回车
    print(s)
    # 移除中间的空格
    print(s.replace(' ',''))
    # 多个空格替换为一个空格
    print(re.sub('\s+', ' ', s))

    # 每行去两边空格
    # with open(filename) as f:
    #     lines = (line.strip() for line in f)
    #     for line in lines:
    #         print(line)

if __name__ == '__main__':
    strip_fun()