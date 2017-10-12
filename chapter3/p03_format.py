#!/usr/bin/env python3
# -*- coding:utf8 -*-

def formatfun():
    x = 1234.56789
    print(format(x,'0.2f'))
    print(format(x, '>10.1f'))
    print(format(x,'^10.1f'))
    print(format(x,','))
    print(format(x,'e'))
    print(format(x,'0.2E'))
    # 同时制定宽度和精度的format格式[<>ˆ]?width[,]?(.digits)?
    print('The value is {:0,.2f}'.format(x))
    # 自己测试
    print('The value is {:^15,.3f}'.format(x))

    swap_separators = { ord('.'):',', ord(','):'.' }
    print(format(x,',').translate(swap_separators))

    print('%0.2f' % x)
    print('%10.1f' % x)
    print('%-10.1f' % x)


if __name__ == '__main__':
    formatfun()