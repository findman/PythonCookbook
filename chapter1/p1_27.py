#!/usr/bin/env python3
# -*- coding:utf8 -*-

nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)
print('s =',s)

import os
files = os.listdir('chapter1')
# print(files)
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# 输出 CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]

# 找最小值
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)