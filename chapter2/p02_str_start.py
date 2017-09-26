#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:字符串开头或结尾匹配
Desc:
"""
import os
import re
from urllib.request import urlopen

def start_str():
    filename = 'spam.txt'
    print(filename.endswith('.txt'))
    print(filename.startswith('file:'))
    url = 'http://www.python.org'
    print(url.startswith('http:'))

    filenames = os.listdir('.')
    print(filenames)    # ['.git', '.vscode', 'chapter1', 'chapter2', 'README.md']

    print([name for name in filenames if name.endswith(('.git','.md'))])
    print(any(name.endswith('.md') for name in filenames))

    # choices = ['http:', 'https:']
    # 注意startswith仅支持元组
    # Traceback (most recent call last):
    # File "d:\Projects\2017\PythonCookbook\PythonCookbook\chapter2\p02_str_start.py", line 37, in <module>
    #     start_str()
    # File "d:\Projects\2017\PythonCookbook\PythonCookbook\chapter2\p02_str_start.py", line 26, in start_str
    #     url.startswith(choices)
    # TypeError: startswith first arg must be str or a tuple of str, not list    
    # url.startswith(choices)

    filename2 = 'spam.txt'
    print(filename2[-4:] == '.txt')
    print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

    # <_sre.SRE_Match object; span=(0, 5), match='http:'>
    print(re.match('http:|https:|ftp:',url))

    # 文件类型检查
    # if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):


def read_data(name)    :
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        # 这里原例有编码问题，因为所有代码格式utf8
        with open(name,encoding='utf-8') as f:
            return f.read()

if __name__ == '__main__':
    start_str()
    # Pass
    #print(read_data('http://www.python.org'))
    # Pass
    #print(read_data('./chapter2/p01_splitstr.py'))
    