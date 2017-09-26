#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:最短匹配，非贪婪模式匹配
Desc:
"""

import re

def short_match():
    # 贪婪模式
    # 默认 '.' '*' '+' 为贪婪模式
    str_pat = re.compile(r'\"(.*)\"')
    text1 = 'Computer says "no."'
    text2 = 'Computer says "no." Phone says "yes."'
    print(str_pat.findall(text1))
    print(str_pat.findall(text2))
    # 在*后添加?实现非贪婪模式
    str_pat = re.compile(r'\"(.*?)\"')
    print(str_pat.findall(text1))
    print(str_pat.findall(text2))    


if __name__ == '__main__':
    short_match()