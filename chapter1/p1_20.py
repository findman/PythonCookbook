#!/usr/bin/env python3
# -*- coding:utf8 -*-

rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows,key = itemgetter('fname'))
# 这里也可以使用匿名函数实现，但效率不如itemgetter
#rows_by_fname = sorted(rows,key =lambda d:d['fname'])
rows_by_lname = sorted(rows, key = itemgetter('lname','fname'))
rows_by_uid = sorted(rows, key = itemgetter('uid'))

print(rows_by_fname)
print('*'*40)
print(rows_by_lname)
print('*'*40)
print(rows_by_uid)

print('*'*40)

# itemgetter函数可以根据key获取值并返回排序依据值
m = min(rows, key = itemgetter('uid'))
x = max(rows, key = itemgetter('uid'))
print(m)
print(x)
