#!/usr/bin/env python3
# -*- coding:utf8 -*-

"""
Topic:审查清理文本字符串
Desc:
"""
import io  
import sys
import unicodedata

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码  

# 简单的replace效率更高
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s

def translate_fun():
    s = 'pýtĥöñ\fis\tawesome\r\n'
    print(s)

    remap = {
        # ord 一个ascii字符
        ord('\t') : ' ',
        ord('\f') : ' ',
        ord('\r') : None
    }
    a = s.translate(remap)
    print(a)
    # 找到所有的和音字符
    cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    # 标准化
    b = unicodedata.normalize('NFD',a)
    print(b.translate(cmb_chrs))

    digitmap = {
        # unicodedata.digit把一个合法的数字字符串转换为数字值
        c: ord('0') + unicodedata.digit(chr(c))
        for c in range(sys.maxunicode)
        # 类型是否为Nd，及数字类型
        if unicodedata.category(chr(c)) == 'Nd'
    }
    print(len(digitmap))

    x = '\u0661\u0662\u0663'
    print(x.translate(digitmap))

    # IO解码与编码处理
    b = unicodedata.normalize('NFD', s)
    print(b.encode('ascii', 'ignore').decode('ascii'))
    print(b.encode('utf-8', 'ignore').decode('utf-8'))

if __name__ == '__main__':
    translate_fun()