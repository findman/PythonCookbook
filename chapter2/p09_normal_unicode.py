#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:将 Unicode 文本标准化
Desc:
"""
import unicodedata

def normal_unicode():
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'

    #print(s1)
    #print(s2)

    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)

    print(t1 == t2)
    print(ascii(t1))

    t3 = unicodedata.normalize('NFD', s1)
    t4 = unicodedata.normalize('NFD', s2)

    print(t3 == t4)
    print(ascii(t3))

    s = '\ufb01'
    #print(s)
    s1 = unicodedata.normalize('NFD', s)
    s2 = unicodedata.normalize('NFKD', s)
    s3 = unicodedata.normalize('NFKC', s)
    print(ascii(s1))
    print(ascii(s2))
    print(ascii(s3))

    #print(''.join(c for c in t1 if not unicodedata.combining(c)))


if __name__ == '__main__':
    normal_unicode()