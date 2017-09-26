#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:字符串对齐
Desc:
"""

def align_str():
    text = 'Hello World'
    # 20个字符不足在左边补齐
    print(text.ljust(20))
    # 20个字符不足在右边补齐
    print(text.rjust(20))
    # 20个字符不足在左右边补齐    
    print(text.center(20))
    # 20个字符不足在左边用'='补齐    
    print(text.rjust(20, '='))
    # 20个字符不足在左右边用'*'补齐
    print(text.center(20, '*'))

    # format实现
    # 20个字符不足在左边补齐
    print(format(text, '>20'))
    # 20个字符不足在右边补齐
    print(format(text, '<20'))
    # 20个字符不足在左右边补齐
    print(format(text, '^20'))
    # 20个字符不足在左边用'='补齐   
    print(format(text, '=>20s'))
    # 20个字符不足在左右边用'*'补齐
    print(format(text, '*^20s'))
    # 每个词10个字符不足空格补齐
    print('{:>10s} {:>10s}'.format('Hello','World'))
    
    x = 1.2345
    # 10个字符左边补齐
    print(format(x, '>10'))
    # 10个字符左右补齐，保持两位小数
    print(format(x, '^10.2f'))

    # old code
    print('%-20s' % text)
    print('%20s' % text)

if __name__ == '__main__':
    align_str()