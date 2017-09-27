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

#### 2.9 将 Unicode 文本标准化
- `unicodedata.normalize` 标准化unicode
- `unicodedata.combining`判断是否为和音字符

#### 2.10 在正则式中使用 Unicode
- `re`默认支持Unicode
- 建议先标准化并清理所有文本
- 忽略大小写
- Unicode中重音符号有两种表示方法，用一个字节表示，或者用基字母加上重音符号表示，在Unicode中他们是相等的，但是在Python中由于通过code point来比较大小，所以就不相等了。
>解决方法是通过unicodedata库中的normalize函数，该函数的第一个参数可以接受"NFC",'NFD','NFKC','NFKD'四个参数中的一个。
>NFC(Normalization Form Canonical Composition)：以标准等价方式来分解，然后以标准等价重组之。若是singleton的话，重组结果有可能和分解前不同。尽可能的缩短>整个字符串的长度，所以会把'e\u0301'2个字节压缩到一个字节'é'。
>NFD(Normalization Form Canonical Decomposition)：以标准等价方式来分解
>NFKD(Normalization Form Compatibility Decomposition)：以相容等价方式来分解
>NFKC(Normalization Form Compatibility Composition)：以相容等价方式来分解，然后以标准等价重组之。
>NFKC和NFKD可能会引起数据损失。

#### 2.11 删除字符串中不需要的字符
- `strip`去两边空格，也可输入多个字符，并在两端除去
- `lstrip`、`rstrip` 移除左边和右边空格，也可输入多个字符
-  注意`strip`仅移除左右两侧的空格和回车
-  移除中间空格可用`replace`
-  更复杂的用正则

#### 2.12 审查清理文本字符串
- `translate(remap)`有点类似字符替换

#### 2.13 字符串对齐
- `ljust`,`rjust` ,`center` 处理对其
- `format` 使用`>`,`<`,`^` 处理对其

#### 2.14 合并拼接字符串
- 连接字符可以用`+`,`join`,`format`，还是可以生成器进行字符串转换
- 简单的连接最好用`print`函数的`sep`参数
- 大量数据建议使用生成器函数

#### 2.15 字符串中插入变量
- `format()`、`format map()`格式化字符串
- `__missing__`处理key缺失的情况
- 函数使用 sys.getframe(1) 返回调用者的栈帧
- 可以从中访问属性f_locals 来获得局部变量

#### 2.16 以指定列宽格式化字符串
- `textwrap.fill` 控制指定宽度
- `initial_indent` 开始字符串
- `subsequent_indent`第二行开始的字符串

#### 2.17 在字符串中处理 html 和 xml
- `html.escape(s)`转换特殊字符
- 非ASCII嵌入`s.encode('ascii', errors='xmlcharrefreplace')`
- `HTMLParser()`类型`p.unescape(s)` 转码

#### 2.18 字符串令牌解析
- Python专有的正则模式命令组。(?P<name>...) 成组之后，name为组。[参考](https://wizardforcel.gitbooks.io/py-re-guide/content/14.html)
- 正则预编译后有`scanner`函数，它每次逐一扫描出字符串中的匹配项
- `iter`函数创建一个可以一次迭代一个元素的对象.函数原型`iter(object[, sentinel])`.[参考](https://www.programiz.com/python-programming/methods/built-in/iter)
- 实现字符串令牌化，需要实现生成器函数，迭代执行scanner函数，将匹配结果逐一输出


#### 2.19 实现一个简单的递归下降分析器
- 暂时看不太明白。以后在研究


#### 2.20 字节字符串上的字符串操作
- 基本和字符串处理相同