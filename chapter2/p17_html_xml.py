#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:处理html和xml文本
Desc:
"""
import io
import sys
import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码  

def html_xml():
    s = 'Elements are written as "<tag>text</tag>".'
    print(s)
    print(html.escape(s))

    # Disable escaping of quotes
    print(html.escape(s, quote=False))

    s = 'Spicy Jalapeño'
    print(s.encode('ascii', errors='xmlcharrefreplace'))

    s = 'Spicy &quot;Jalape&#241;o&quot.'
    p = HTMLParser()
    print(p.unescape(s))

    t = 'The prompt is &gt;&gt;&gt;'
    print(unescape(t))

if __name__ == '__main__':
    html_xml()