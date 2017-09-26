#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:多行匹配
Desc:
"""

import re

def multiline_match():
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''/* this is a
    multiline comment */
    '''

    print(comment.findall(text1))
    print(comment.findall(text2))

    #(?:.|\n) 非组匹配，匹配内容是出换行以外的字符或换行符
    comment = re.compile(r'/\*((?:.|\n)*?)\*/')

    print(comment.findall(text1))
    print(comment.findall(text2))

    #  re.DOTALL标志可以让点匹配换行符
    comment = re.compile(r'/\*((?:.|\n)*?)\*/', flags=re.DOTALL)
    print(comment.findall(text1))
    print(comment.findall(text2))  

if __name__ == '__main__':
    multiline_match()