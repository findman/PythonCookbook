#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:在正则式中使用 Unicode
Desc:
"""
import io  
import sys 
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码  

def re_unicode():
    num = re.compile('\d+')
    print(num.match('123'))
    print(num.match('\u0661\u0662\u0663'))
    arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
    pat = re.compile('stra\u00dfe', re.IGNORECASE)
    s = 'straße'
    print(pat.match(s)) # Matches
    pat.match(s.upper()) # Doesn't match
    print(s.upper())

if __name__ == '__main__':
    re_unicode()