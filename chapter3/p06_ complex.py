#!/usr/bin/env python3
# -*- coding:utf8 -*-

a = complex(2, 4)
b = 3 - 5j
print('a:', a)
print('b:', b)
print('a.real:', a.real)
print('a.imag:', a.imag)
print('a.conjugate():', a.conjugate())
print('a + b:', a + b)
print('a * b:', a * b)
print('a / b:', a / b)
print('abs(a):', abs(a))

import cmath
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

import numpy as np
a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
print(a)
print(a + 2)
print(np.sin(a))

import math
# math.sqrt(-1)
