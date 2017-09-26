#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:格式化字符串为指定宽度
Desc:
"""
import textwrap
import os

def reformat_width():
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."

    print(textwrap.fill(s, 70))
    print('='*80)
    print(textwrap.fill(s, 40))
    print('='*80)    
    print(textwrap.fill(s, 40, initial_indent='    '))
    print('='*80)    
    print(textwrap.fill(s, 40, subsequent_indent=' '))
    

    #size = os.get_terminal_size().columns

if __name__ == '__main__':
    reformat_width()