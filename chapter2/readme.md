## 第二章：字符串和文本


#### 2.1 使用多个界定符分割字符串
- 在`re.split`中使用组时，组也会作为分割结果
- `(?: re)` 类似 `(...)`, 但是不表示一个组
- Python正则参考[Link](http://www.runoob.com/python/python-reg-expressions.html)

#### 2.2 字符串开头或结尾匹配
- 一般使用`startswith`和`endswith`检查头尾就够用了
- 注意输入值仅支持元组，其他序列输入需要进行转换