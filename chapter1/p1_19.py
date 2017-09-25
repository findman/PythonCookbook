#!/usr/bin/env python3
# -*- coding:utf8 -*-

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)

# 出现频率最高的三个词
top_three = word_counts.most_common(3)

print(top_three)
print(word_counts)

morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
print(word_counts)

for word in morewords:
    word_counts[word] += 1
print(word_counts)

print('*'*40)
# Counter计算
a = Counter(words)
b = Counter(morewords)

print('a =',a)
print('b =',b)

c = a + b
print('c =',c)

d = a - b
print('d =',d)


