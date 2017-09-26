#!/usr/bin/env python3
# -*- coding:utf8 -*-
"""
Topic:字符串令牌化
Desc:
"""

import re
from collections import namedtuple

# 生成器函数
def generate_tokens(pat, text):
    Token = namedtuple('Token',['type','value'])
    scanner = pat.scanner(text)
    # iter函数创建一个可以一次迭代一个元素的对象
    # iter(object[, sentinel])
    # https://www.programiz.com/python-programming/methods/built-in/iter
    for m in iter(scanner.match,None):
        yield Token(m.lastgroup,m.group())


def tokenize_str():
    text = 'foo = 23 + 42 * 10'
    tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
    # 命令组 (?P<name>...) 成组之后，name为组名
    # https://wizardforcel.gitbooks.io/py-re-guide/content/14.html
    NAME = r'(?P<NAME>[a-zA-Z][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'



    print('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
    scanner = master_pat.scanner('foo = 42')
    
    #print(type(master_pat))
    #print(type(scanner))
    
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)


    # Example use
    for tok in generate_tokens(master_pat, 'foo = 42'):
        print(tok)


if __name__ == '__main__':
    tokenize_str()