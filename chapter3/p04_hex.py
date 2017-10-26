#!/usr/bin/env python3
# -*- coding:utf8 -*-


def ts_fun():
    x = 1234
    print(bin(x))
    print(oct(x))
    print(hex(x))

    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))

    x = -1234
    print(format(x, 'b'))
    print(format(x, 'x'))

    print(format(2**32 + x, 'b'))
    print(format(2 * 32 + x, 'x'))

    print(int('4d2', 16))
    print(int('10011010010', 2))


if __name__ == '__main__':
    ts_fun()
