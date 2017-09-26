#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:字符串合并
Desc:
"""

def join_str():
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print(' '.join(parts))
    print(','.join(parts))
    print(''.join(parts))
    a = 'Is Chicago'
    b = 'Not Chicago?'
    print(a + ' ' + b)
    print('{} {}'.format(a,b))

    a = 'Hello' 'World'
    print(a)

    # 加法操作效率较低，因为会引起内存复制及垃圾回收
    # s = ''
    # for p in parts:
    #     s += p

    # 利用生成器
    data = ['ACME', 50, 91.1]
    print(','.join(str(d) for d in data))

    c = 'Yes'
    print(a + ':' + b + ':' + c) # Ugly
    print(':'.join([a, b, c])) # Still ugly
    # 最优方案
    print(a, b, c, sep=':') # Better    

if __name__ == '__main__':
    join_str()