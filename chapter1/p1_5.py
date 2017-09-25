#!/usr/bin/env python3
# -*- coding:utf8 -*-

# 字符串处理
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print('uname:',uname)
print('homedir:',homedir)
print('sh:',sh)

print('='*30)

# 数据丢弃
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print('name:',name)
print('year:',year)