from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

# 让原对象替换模板对象实现填充具有可选或缺失的命名元组
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
a = dict_to_stock(a)
print(a)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
b = dict_to_stock(b)
print(b)