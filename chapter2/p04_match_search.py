#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic: 字符串匹配和搜索
Desc : 
"""
import  re

def match_search():
    # 常规字符串处理
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text == 'yeah')
    print(text.startswith('yeah'))
    print(text.endswith('no'))
    # find查找第一个匹配对象
    print(text.find('no'))

    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'

    if re.match(r'\d+/\d+/\d+', text1):
        print('yes')
    else:
        print('no')

    if re.match(r'\d+/\d+/\d+', text2):
        print('yes')
    else:
        print('no')

    # 如果需要多次匹配，可以先将正则预编译
    datepat = re.compile(r'\d+/\d+/\d+')
    if datepat.match(text1):
        print('yes')
    else:
        print('no')

    if datepat.match(text2):
        print('yes')
    else:
        print('no')  

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'              
    print(datepat.findall(text))

    # 正则分组
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = datepat.match('11/27/2012')
    month, day, year = m.groups()
    print('month',month)
    print('day',day)
    print('year',year)


    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print(datepat.findall(text))

    # 分组重组
    for month, day, year in datepat.findall(text):
        print('{}-{}-{}'.format(year, month, day))
    
    # match 匹配从头开始如果需要从确定结尾使用$
    m = datepat.match('11/27/2012abcdef')
    print(m)

    datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
    print(datepat.match('11/27/2012abcdef'))
    print(datepat.match('11/27/2012')

    # 单一操作就不需要预编译了。。。。。

if __name__ == '__main__':
    match_search()