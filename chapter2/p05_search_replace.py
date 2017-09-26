#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:字符串搜索和替换
Desc:
"""


import re
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{}-{}-{}'.format(m.group(2),mon_name,m.group(3))


def match_search():
    text = 'yeah, but no, but yeah, but no, but yeah'
    # 这里需要注意一点它不会对原数据进行修改，而是返回一个新字符串
    print(text.replace('yeah', 'yep'))
    #print(text)

    # 复杂模式，可以使用re 模块中的 sub()函数
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    # 第二个参数中的1，2，3分别对应第一个参数中的正则组
    print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

    # 和所有正则一样，反复用请预编译
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat.sub(r'\3-\1-\2', text))

    # 复杂请用处理函数
    print(datepat.sub(change_date,text))

    # 如果想知道发送了几次替换请使用subn
    newtext, n = datepat.subn(r'\3-\1-\2', text)
    print('newtext:', newtext)
    print('num:', n)

if __name__ == '__main__':
    match_search()