#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:字符串中的变量
Desc:
"""
import sys
import string

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n      

class safesub(dict):
    """ 防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'

def sub(text):
    # 函数使用 sys.getframe(1) 返回调用者的栈帧
    # 可以从中访问属性f_locals 来获得局部变量
    return text.format_map(safesub(sys._getframe(1).f_locals))    

def var_string():
    s = '{name} has {n} messages.'
    print(s.format(name = 'Guido', n = 37))
    name = 'Guido'
    n = 37
    print(vars())
    print(s.format_map(vars()))
    a = Info('Guido', 37)
    print(vars(a))
    print(s.format_map(vars(a)))    

    # format和format_map()的缺陷不能很好的处理变量缺失
    # s.format(name='Guido')
    # Traceback (most recent call last):
    # File "f:\Projects\2017\PythonCookbook\chapter2\p15_var_string.py", line 29, in <module>
    # var_string()
    # File "f:\Projects\2017\PythonCookbook\chapter2\p15_var_string.py", line 26, in var_string
    # s.format(name='Guido')
    # KeyError: 'n'

    # del n
    print(s.format_map(safesub(vars())))

    print(sub('Hello {name}'))
    print(sub('You have {n} messages.'))
    print(sub('Your favorite color is {color}'))
    # print('%(name) has %(n) messages.' % vars())
    s = string.Template('$name has $n messages.')
    print(s.substitute(vars()))

if __name__ == '__main__':
    var_string()