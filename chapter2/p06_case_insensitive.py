#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic: 字符串忽略大小写的搜索替换
Desc : 
"""

import re

def matchcase(word):
    def replace(m):
        text = m.group()
        #print(text)
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

def case_insensitive():
    text = 'UPPER PYTHON, lower python, Mixed Python'
    # re.IGNORECASE忽略大小写
    print(re.findall('python', text, flags=re.IGNORECASE))
    print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
    # 这里matchcase 返回的是replace函数，来处理snake
    print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

if __name__ == '__main__':
    case_insensitive()