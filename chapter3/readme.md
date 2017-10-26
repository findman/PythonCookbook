## 第三章：数字日期和时间

#### 3.1 数字的四舍五入
- `round(value, ndigits)`，设置精度
- `format`格式化。`format(x, '0.2f')`

#### 3.2 执行精确的浮点数运算
- 精确计算需要使用`decimal`模块
- `math.fsum()`精确求和


#### 3.3 数字的格式化输出
- 同时制定宽度和精度的format格式[<>ˆ]?width[,]?(.digits)?

#### 3.4 二八十六进制整数
- `bin()`整数转二进制
- `oct()`整数转八进制
- `hex()`整数转十六进制
- `format()`格式化'b,o,x'分别对应二进制、八进制、十六进制

#### 3.5 字节到大整数的打包与解包
- 字节转整数`int.from_bytes(data, 'little')`、`int.from_bytes(data, 'big')`
- Little endian：将低序字节存储在起始地址
- Big endian：将高序字节存储在起始地址
- x.to_bytes(4, 'big|little')整数转字节
- divmod(a,b) 本函数是实现a除以b，然后返回商与余数的元组