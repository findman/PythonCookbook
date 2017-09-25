#!/usr/bin/env python3
# -*- coding:utf8 -*-

# 去头去尾，嘎嘣脆
# 去掉首尾，求平均值
grades = (1, 2, 3, 4, 5, 6, 7, 8, 9 ,10)

def avg(middle):
    l = len(middle)
    s = sum(middle)
    return s/l

def drop_first_last(grades):
    # 星号获取一个列表类型
    first, *middle, last = grades
    return avg(middle)

print('avg =',drop_first_last(grades))

# 星号获取多个值案例2
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print('name =',name)
print('email =',email)
print('phone_numbers =',str(phone_numbers))

# 读取前部多个数据
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print('trailing =',str(trailing))
print('current =',current)