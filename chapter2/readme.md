## 第二章：字符串和文本


#### 2.1 使用多个界定符分割字符串
- 在`re.split`中使用组时，组也会作为分割结果
- `(?: re)` 类似 `(...)`, 但是不表示一个组
- [Python正则参考](http://www.runoob.com/python/python-reg-expressions.html)

#### 2.2 字符串开头或结尾匹配
- 一般使用`startswith`和`endswith`检查头尾就够用了
- 注意输入值仅支持元组，其他序列输入需要进行转换

#### 2.3 用 Shell 通配符匹配字符串
- `fnmatch`, `fnmatchcase` 其中`fnmatchcase`对大小敏感
- 功能处于字符串处理和正则之间

#### 2.4 字符串匹配和搜索
- 主要是正则，参考2.1中的Python正则参考

#### 2.5 字符串搜索和替换
- 简单的用`str`的`replace`
- 复杂的用`re`的`sub`
- 更复杂的创建处理函数再丢个`sub`
- 如果要知道替换了几次用`subn`

#### 2.6 字符串忽略大小写的搜索替换
- `re.IGNORECASE`忽略大小写

#### 2.7 最短匹配模式
- 默认 '.' '*' '+' 为贪婪模式
- 在其后添加'?'则为非贪婪模式
- ‘.’ 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。

#### 2.8 多行匹配模式
- `re.DOTALL`标志可以让点匹配所有字符包含换行符
- 不使用这个标志则需要使用或匹配把换行符放进去

#### 将 Unicode 文本标准化
- `unicodedata.normalize` 标准化unicode
- `unicodedata.combining`判断是否为和音字符