#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:正则式分割字符串
Desc:
"""
import re

def split_str():
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    # [...] 用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
    # \s 匹配任意空白字符，等价于 [\t\n\r\f].
    # re* 匹配0个或多个的表达式。
    # 正则解释一个';'、',','任意空白字符'，接0个或多个任意空白字符
    print(re.split(r'[;,\s]\s*',line))

    # (re) G匹配括号内的表达式，也表示一个组
    # 在re.split中使用组时，组也会作为分割结果
    fields = re.split(r'(;|,|\s)\s*',line)
    print(fields)

    # 从0开始，以2为进步，将获取所有的值    
    values = fields[::2]
    print('values:',values)
    # 从1开始，以2为进步，获取所有分割符。最后加入一个空字符用于后面链接时一一匹配
    # 否则会因为长度不同无法构建字典结构
    delimiters = fields[1::2] + ['']
    print('delimiters:',delimiters)

    # 查看表达式内部过程
    for v, d in zip(values,delimiters):
        print('v:',v)
        print('d:',d)
    
    print('*'*40)

    # Reform the line using the same delimiters
    print(''.join(v+d for v, d in zip(values,delimiters)))

    # (?: re) 类似 (...), 但是不表示一个组
    print(re.split(r'(?:;|,|\s)\s*',line))

if __name__ == '__main__':
    split_str()