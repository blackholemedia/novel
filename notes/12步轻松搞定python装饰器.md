# 1.函数的作用域(命名空间)
&emsp;&emsp; <font size=5>python中，函数会创建一个新的作用域(命名空间)，意味着在函数内部碰到一个变量的时候函数会优先在自己的命名空间里面去寻找</font>

```python
a_string = "This is a global variable"
def foo():
     print locals()

print globals() # 打印全局作用域变量
{, 'a_string': 'This is a global variable'}
foo() # 打印本地作用域变量
{}
```

# 2.变量解析规则<br>
&emsp;&emsp; <font size=5>在python的作用域规则里面，创建变量一定会在当前作用域里创建一个变量，但访问或修改变量时会先在当前作用域查找变量，没有找到则会依次向上在闭合的作用域里面进行查找：</font>

```python
a_string = "This is a global variable"
def foo():
     print a_string # 1
foo()
This is a global variable
```
&emsp;&emsp; <font size=5>全局变量能够被访问到（如果是可变数据类型(像list,dict这些)甚至能够被更改），但是赋值不行。在函数内部的#1处，我们实际上新创建了一个局部变量，隐藏全局作用域中的同名变量</font>

```python
a_string = "This is a global variable"
def foo():
     a_string = "test" # 1
     print locals()
foo()
{'a_string': 'test'}
a_string # 2
'This is a global variable'
```

# 3.变量生存周期
```python
def foo():
     x = 1
foo()
print x # 1
Traceback (most recent call last):

NameError: name 'x' is not defined
```
&emsp;&emsp; <font size=5>#1处发生的错误不仅仅是因为作用域规则导致的（尽管这是抛出了NameError的错误的原因）,变量x此时不存在！函数foo的命名空间随着函数调用开始而开始，结束而销毁</font>

# 4.函数参数
&emsp;&emsp; <font size=5>python允许我们向函数传递参数，参数会变成本地变量存在于函数内部，函数的参数可以是必须的位置参数+可选的命名，默认参数</font>
```python
def foo(x, y=0): # 1
     return x - y
foo(3, 1) # 2
2
foo(3) # 3
3
foo() # 4
Traceback (most recent call last):

TypeError: foo() takes at least 1 argument (0 given)
foo(y=1, x=3) # 5
2
```
&emsp;&emsp; <font size=5>#1处我们定义了函数foo,它有一个位置参数x和一个命名参数y，#5处的函数调用，我们传递的是两个命名实参，这个时候因为有名称标识，参数传递的顺序也就不用在意了</font>

# 5.嵌套函数
&emsp;&emsp; <font size=5>Python允许创建嵌套函数。这意味着我们可以在函数里面定义函数而且现有的作用域和变量生存周期依旧适用：</font><br>
```python
def outer():
     x = 1
     def inner():
         print x # 1
     inner() # 2

outer()
1
```
&emsp;&emsp; <font size=5>在#1处python解释器需找一个叫x的本地变量，查找失败之后会继续在上层的作用域里面寻找，这个上层的作用域定义在另外一个函数里面，python解释器会优先在outer的作用域里面对变量名inner查找匹配的变量</font>

# 6.函数是python世界里的一级类对象
&emsp;&emsp; <font size=5> 在python里，函数和其他东西一样都是对象，**即可以把函数像参数一样传递给其他的函数或者说别的函数里面返回函数**</font>
```python
def add(x, y):
     return x + y
def sub(x, y):
     return x - y
def apply(func, x, y): # 1
     return func(x, y) # 2
apply(add, 2, 1) # 3
3
apply(sub, 2, 1)
1
```
&emsp;&emsp; <font size=5> 在#1处你们能看到准备接收一个函数m名的变量，和其他变量一样。在#2处我们调用传进来的函数：“()代表着调用的操作并且调用变量包含的值。在#3处，函数的名称只是很其他变量一样的标识符而已</font>
```python
def outer():
     def inner():
         print "Inside inner"
     return inner # 1

foo = outer() #2
foo # doctest:+ELLIPSIS
<function inner at 0x>
foo()
Inside inner
```
&emsp;&emsp; <font size=5> 在#1处我把**恰好**是函数标识符的变量inner作为返回值返回出来。这并没有什么特殊的语法：“把函数inner返回出来，否则它根本不可能会被调用到”。还记得变量的生存周期吗？每次函数outer被调用的时候，函数inner都会被重新定义，如果它不被当做变量返回的话，每次执行过后它将不复存在</font>
&emsp;&emsp; <font size=5> 在#2处我们捕获住返回值 – 函数inner，将它存在一个新的变量foo里。我们能够看到，当对变量foo进行求值，它确实包含函数inner，而且我们能够对它进行调用</font>

# 7.闭包

```python
def outer():
     x = 1
     def inner():
         print x # 1
     return inner
foo = outer()
foo.func_closure # doctest: +ELLIPSIS
(<cell at 0x: int object at 0x>,)
```
&emsp;&emsp; <font size=5> 根据作用域规则：x是函数outer里的一个局部变量。当函数inner在#1处打印x的时候，python解释器会在inner内部查找相应的变量，当然会找不到，所以接着会到封闭作用域里面查找，并且会找到匹配</font>
&emsp;&emsp; <font size=5>根据变量的生存周期：变量x是函数outer的一个本地变量，这意味着只有当函数outer正在运行的时候才会存在。根据我们已知的python运行模式，我们没法在函数outer返回之后继续调用函数inner，在函数inner被调用的时候，变量x早已不复存在，可能会发生一个运行时错误</font>
&emsp;&emsp; <font size=5>实际上inner能够正常工作。Python支持一个叫做函数闭包的特性，即：**嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间**。这能够通过查看函数的func_closure属性得出结论，这个属性里面包含封闭作用域里面的值（只会包含被捕捉到的值，比如x，如果在outer里面还定义了其他的值，封闭作用域里面是不会有的)</font>
&emsp;&emsp; <font size=5>每次函数outer被调用的时候，函数inner都会被重新定义。但变量x的值不会变化，因此每次返回的函数inner会是同样的逻辑</font>

```python
def outer(x):
     def inner():
         print x # 1
     return inner
print1 = outer(1)
print2 = outer(2)
print1()
1
print2()
2
```
&emsp;&emsp; <font size=5> 从这个例子中你能够看到闭包——被函数记住的封闭作用域 ——能够被用来创建自定义的函数</font>

# 8.装饰器

&emsp;&emsp; <font size=5> 装饰器其实就是一个闭包，把一个函数当做参数然后返回一个替代版函数</font>

# 9.Windows环境下文件路径表示

&emsp;&emsp; <font size=5> Python代码里面，反斜杠“\”是转义符，例如“\n”表示回车，采用以下三种方式表示路径</font> 
- <font size=5>  斜杠“/”，如“c:/test.txt”</font><br>
- <font size=5>两个反斜杠“\\\\”，如“c:\\test.txt”</font><br>
- <font size=5>字符串前面加上字母`r`，表示后面是一个原始字符串raw string，如“r“c:\\test.txt””</font>

# 9.Python接收命令行参数

```python
from sys import argv
print(argv)
>>>python xx.py xxx
>>>['xx.py','xxx']
```
&emsp;&emsp; <font size=5> 导入argv，结果即为参数列表</font>

# 10.'\u'前缀字符串

&emsp;&emsp; <font size=5> `\u4f60`十六进制代表对应汉字的utf-16编码</font>

# 11.定义1个元素的tuple

&emsp;&emsp; <font size=5> 定义1个元素的tuple: `>>> t = (1,)`，加上一个逗号，避免成为数学意义上的括号</font>


# 12.from...import与import的区别
- &emsp;&emsp; <font size=5> from  文件夹名/py文件名/模块  import 类名(函数名)，导入的是模块的函数，使用时直接使用函数名即可</font>
- &emsp;&emsp; <font size=5> import 文件夹名/py文件名/模块，导入的是模块，使用时候需要加上模块前缀： `module.fuction()`</font>



# <font size = 8>附录</font>
# <span id="ap1"> 1.方法解析顺序（Method Resolution Order, MRO）列表 </span>
&emsp;&emsp; <font size=5>MRO 列表的顺序遵循以下三条原则：</font><br>
   - &emsp;&emsp;<font size=5>类永远在父类前面</font><br>
   - &emsp;&emsp;<font size=5>如果有多个父类，会根据它们在列表中的顺序被检查</font><br>
   - &emsp;&emsp;<font size=5>如果对下一个类存在两个合法的选择，选择第一个父类</font><br>

# <span id="ap2"> 2.查询模块的帮助文档 </span>
  - &emsp;&emsp;<font size=5>先导入模块，再查询普通模块的使用方法：`help(module_name)`，例：`help(math)`</font><br>
  - &emsp;&emsp;<font size=5>先导入sys，再查询系统内置模块的使用方法：`sys.bultin_modulenames`</font><br>
  - &emsp;&emsp;<font size=5>查看模块下所有函数：`dir(module_name)`，例：`dir(math)`</font><br>
  - &emsp;&emsp;<font size=5>查看模块下特定函数：`help(module_name.func_name)`，例：`help(math.sin)`</font><br>  
  - &emsp;&emsp;<font size=5>查看函数信息的另一种方法：`print(func_name.__doc__)`，例：`print(sin.__doc__)`</font><br>  


# <span id="ap3"> 3.python中时间日期格式化符号 </span>
  - &emsp;&emsp;<font size=5>  %y 两位数的年份表示（00-99）</font><br>
  - &emsp;&emsp;<font size=5> %Y 四位数的年份表示（000-9999）</font><br>
  - &emsp;&emsp;<font size=5> %m 月份（01-12）</font><br>
  - &emsp;&emsp;<font size=5> %d 月内中的一天（0-31）</font><br> 
  - &emsp;&emsp;<font size=5> %H 24小时制小时数（0-23）</font><br> 
  - &emsp;&emsp;<font size=5> %I 12小时制小时数（01-12）</font><br> 
  - &emsp;&emsp;<font size=5> %M 分钟数（00=59）</font><br> 
  - &emsp;&emsp;<font size=5> %S 秒（00-59）</font><br> 
  - &emsp;&emsp;<font size=5> %a 本地简化星期名称</font><br> 
  - &emsp;&emsp;<font size=5> %A 本地完整星期名称</font><br> 
  - &emsp;&emsp;<font size=5> %b 本地简化的月份名称</font><br> 
  - &emsp;&emsp;<font size=5> %B 本地完整的月份名称</font><br> 
  - &emsp;&emsp;<font size=5> %c 本地相应的日期表示和时间表示</font><br> 
  - &emsp;&emsp;<font size=5> %j 年内的一天（001-366）</font><br> 
  - &emsp;&emsp;<font size=5> %p 本地A.M.或P.M.的等价符</font><br> 
  - &emsp;&emsp;<font size=5> %U 一年中的星期数（00-53）星期天为星期的开始</font><br> 
  - &emsp;&emsp;<font size=5> %w 星期（0-6），星期天为星期的开始</font><br> 
  - &emsp;&emsp;<font size=5> %W 一年中的星期数（00-53）星期一为星期的开始</font><br> 
  - &emsp;&emsp;<font size=5> %x 本地相应的日期表示</font><br> 
  - &emsp;&emsp;<font size=5> %X 本地相应的时间表示</font><br> 
  - &emsp;&emsp;<font size=5> %Z 当前时区的名称</font><br> 
  - &emsp;&emsp;<font size=5> %% %号本身</font><br>  