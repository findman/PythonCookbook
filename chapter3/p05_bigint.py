#!/usr/bin/env python3
# -*- coding:utf8 -*-

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print(len(data))

# Little endian：将低序字节存储在起始地址
# Big endian：将高序字节存储在起始地址
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

print(data)

import struct
hi, lo = struct.unpack('>QQ', data)
print(hi)
print(lo)
print((hi << 64) + lo)

x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

x = 523 ** 23
print(x)

# x.to_bytes(16, 'little')
print(x.bit_length())

# divmod(a,b) 本函数是实现a除以b，然后返回商与余数的元组。
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))
