#!/usr/bin/env python3
# -*- coding:utf8 -*-

items = [1, 10, 7, 4, 5, 9]
items2 = [2]

head, *tail = items
print('head:',head)
print('tail:',tail)

print("="*30)

# 这里修改了一下函数名，不然太容易误解了(/ □ \)
# 这里是通递归实现累加，结束条件是tail是否为空
def sumitems(items):
    head, *tail = items
    # print('head:',head)
    # print('tail:',tail)
    return head + sumitems(tail) if tail else head

print(sumitems(items))
