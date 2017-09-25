#!/usr/bin/env python3
# -*- coding:utf8 -*-

from collections import deque
import os

# 生成器函数
def search(lines, pattern, history = 5):
    # 最大队列长度设置为5，抛弃之前的数据，只保留最后的5行
    previous_lines = deque(maxlen = history)
    for li in lines:
        # 找到对应的字符串并返回
        if pattern in li:
            # 返回查找字符串所在行，和它前面的五行
            yield li, previous_lines
        # 不断将行插入
        previous_lines.append(li)

# Example use on a file
if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    with open(path + '/' + 'somefile.txt') as f:
        # 通过生成器函数迭代获取查找结果
        for line, prevlines in search(f, 'python', 5):
            # 打印出前五行
            for pline in prevlines:
                print('[Prevlines]' + pline,end = '')
            # 打印出含python字符串所在行
            print('[Search Result:]' + line, end = '')
            print('-'*20)