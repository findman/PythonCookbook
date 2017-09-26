#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:字符串合并
Desc:
"""

"""
返回数据流程
['Is']
2
Is
['Is', 'Chicago']
9
Is Chicago
['Is', 'Chicago', 'Not']
12
Is Chicago Not
['Is', 'Chicago', 'Not', 'Chicago?']
20
Is Chicago Not Chicago?
"""

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        print(parts)
        size += len(part)
        print(size)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
            print('do something.')
        print(' '.join(parts))
        yield ' '.join(parts) + '<<<<'



def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

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

    # 写文件，短字符串用加号就够了。长字符串建议使用分次写入，减少内存消耗
    # # Version 1 (string concatenation)
    # f.write(chunk1 + chunk2)
    # # Version 2 (separate I/O operations)
    # f.write(chunk1)
    # f.write(chunk2)

    # 大量文字建议使用生成器函数
    text = ' '.join(sample())
    print(text)

    # 也可以IO写入
    # for part in sample():
    #     f.write(part)    

    # 结合文件操作
    with open('./chapter2/filename', 'w') as f:
        for part in combine(sample(), 32768):
            f.write(part)

if __name__ == '__main__':
    join_str()