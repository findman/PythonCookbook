#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:用 Shell 通配符匹配字符串
Desc:
"""

from fnmatch import fnmatch, fnmatchcase

def unix_shell_str():
    print('foo.txt', '*.txt')
    print('foo.txt', '?oo.txt')
    print('Dat45.csv', 'Dat[0-9]*')
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print([name for name in names if fnmatch(name, 'Dat*.csv')])

    # 大小写敏感，使用fnmatchcase
    print(fnmatchcase('foo.txt', '*.TXT'))

    addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
    ]

    print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
    print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

if __name__ == '__main__':
    unix_shell_str()