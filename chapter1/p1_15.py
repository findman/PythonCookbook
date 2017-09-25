#!/usr/bin/env python3
# -*- coding:utf8 -*-
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3,
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2,
}

# Find keys in common
k = a.keys() & b.keys()
print('k:',k)
print(a.keys())     #dict_keys(['y', 'x', 'z'])
# print(type(a.keys()))
# print(dir(a.keys()))

# for key in a.keys():
#     print(key)

# Find keys in a that are not in b
k2 = a.keys() - b.keys()
print('k2:',k2)



# Find (key, value) pairs in common
k3 = a.items() & b.items()
print('k3:',k3)
print(a.items())    # dict_items([('y', 2), ('x', 1), ('z', 3)])
# print(type(a.items()))
# print(dir(a.items()))

k4 = a.items() - b.items()
print('k4:',k4)

# 排除某些内容
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print('c:',c)