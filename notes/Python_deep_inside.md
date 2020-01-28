
Table of Contents
=================

   * [12步搞定装饰器](#12步搞定装饰器)
      * [阅读说明](#阅读说明)
      * [函数的作用域(命名空间)](#函数的作用域命名空间)
      * [变量解析规则](#变量解析规则)
      * [变量生存周期](#变量生存周期)
      * [函数参数](#函数参数)
      * [嵌套函数](#嵌套函数)
      * [函数是python世界里的一级类对象](#函数是python世界里的一级类对象)
      * [闭包](#闭包)
      * [装饰器](#装饰器)

Created by ALTA
# 12步搞定装饰器  

*<font color=#008000>绿色斜体</font>*代表个人的思考理解，*<font color=Yellow>黄色斜体</font>*代表阅读理解过程中的疑问，<font color=Red>红色正体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息`阴影`或 *一般斜体* 均表示引用或强调 

内容来自[12步轻松搞定python装饰器](<https://www.jianshu.com/p/d68c6da1587a>)， [Understanding Python Decorators in 12 Easy Steps](<https://dzone.com/articles/understanding-python>)  

## 函数的作用域(命名空间)  

python中，函数会创建一个新的作用域(命名空间)，意味着在函数内部碰到一个变量的时候函数会优先在自己的命名空间里面去寻找

```python
a_string = "This is a global variable"
def foo():
     print locals()

print globals() # 打印全局作用域变量
foo() # 打印本地作用域变量
----------------------------------# 输出结果
{, 'a_string': 'This is a global variable'}
{}
```

## 变量解析规则  

在python的作用域规则里面，<u>创建变量一定会在当前作用域里创建一个变量，但访问或修改变量时会先在当前作用域查找变量</u>，没有找到则会依次向上在闭合的作用域里面进行查找

```python
a_string = "This is a global variable"
def foo():
     print a_string  # 1
foo()
----------------------------------# 输出结果
This is a global variable
```

全局变量能够被访问到（如果是可变数据类型(像list,dict这些)甚至能够被更改），但是赋值不行。在函数内部的#1处，我们实际上新创建了一个局部变量，隐藏全局作用域中的同名变量

## 变量生存周期  

<font color=Red>函数的命名空间(作用域)随着函数调用开始而开始，结束而销毁</font>

```python
def foo():
     x = 1
foo()
print x # 1
----------------------------------# 输出结果
Traceback (most recent call last):
NameError: name 'x' is not defined
```

在#1处发生的错误不仅仅是因为作用域规则(*<font color=#008000>空间</font>*)导致的（尽管这是抛出了NameError的错误的原因）,变量x此时不存在！函数foo的命名空间随着函数调用开始而开始，结束而销毁(*<font color=#008000>时间</font>*)

## 函数参数  

python允许我们向函数传递参数，参数会变成本地变量存在于函数内部(*<font color=#008000>作用域和生命周期在函数内部</font>*)，函数的参数可以是必须的位置参数+可选的命名，默认参数

```python
def foo(x, y=0):									# 1
     return x - y
# ----------------------------------
foo(3, 1)													# 2
2
# ----------------------------------
foo(3) 														# 3
3
# ----------------------------------
foo() 														# 4
Traceback (most recent call last):
TypeError: foo() takes at least 1 argument (0 given)
# ----------------------------------
foo(y=1, x=3)											# 5
2
```

在#1处我们定义了函数foo,它有一个位置参数x和一个命名参数y，#5处的函数调用，我们传递的是两个命名实参，这个时候因为有名称标识，参数传递的顺序也就不用在意了

## 嵌套函数  

Python允许创建嵌套函数。这意味着我们可以在函数里面定义函数而且现有的作用域和变量生存周期依旧适用

```python
def outer():
     x = 1
     def inner():
         print x									# 1
     inner()											# 2
outer()
----------------------------------# 输出结果
1
```

在#1处python解释器需找一个叫x的本地变量，查找失败之后会继续在上层的作用域里面寻找，这个上层的作用域定义在另外一个函数里面，python解释器会优先在outer的作用域里面对变量名inner查找匹配的变量  

## 函数是python世界里的一级类对象  

在python里，<font color=red>函数和其他东西一样都是对象，即可以把函数像参数一样传递给其他的函数或者说别的函数里面返回函数</font>

```python
def add(x, y):
     return x + y
def sub(x, y):
     return x - y
def apply(func, x, y):				# 1
     return func(x, y)				# 2
# ----------------------------------
apply(add, 2, 1)							# 3
3
# ----------------------------------
apply(sub, 2, 1)
1
```

在#1处你们能看到准备接收一个函数名的变量，和其他变量一样。在#2处我们调用传进来的函数：<u>()代表着调用的操作并且调用变量包含的值</u>。在#3处，函数的名称只是很其他变量一样的标识符而已

```python
def outer():
     def inner():
         print "Inside inner"
     return inner							# 1

foo = outer()									#2
# ----------------------------------
foo														
<function inner at 0x>
foo()
Inside inner
```

在#1处我把**恰好**是函数标识符的变量inner作为返回值返回出来。这并没有什么特殊的语法：“把函数inner返回出来，否则它根本不可能会被调用到”。还记得变量的生存周期吗？<u>每次函数outer被调用的时候，函数inner都会被重新定义，如果它不被当做变量返回的话，每次执行过后它将不复存在</u>(<font color=green>inner 在outer被调用的时候创建，outer调用结束后销毁</font>)

在#2处我们捕获住返回值 – 函数inner，将它存在一个新的变量foo里。我们能够看到，当对变量foo进行求值，它确实包含函数inner，而且我们能够对它进行调用

## 闭包  

*<font color=green> 函数记住它在被定义时的封闭作用域</font>*

```python
def outer():
     x = 1
     def inner():
         print x 			# 1
     return inner
foo = outer()
# ----------------------------------
foo.func_closure
(<cell at 0x: int object at 0x>,)
```

根据作用域规则：x是函数outer里的一个局部变量。当函数inner在#1处打印x的时候，python解释器会在inner内部查找相应的变量，当然会找不到，所以接着会到封闭作用域里面查找，并且会找到匹配  

根据变量的生存周期：变量x是函数outer的一个本地变量，这意味着只有当函数outer正在运行的时候才会存在。根据我们已知的python运行模式，我们没法在函数outer返回之后继续调用函数inner，<u>在函数inner被调用的时候，变量x早已不复存在，可能会发生一个运行时错误</u>  

实际上inner能够正常工作。Python支持一个叫做函数闭包的特性，即：**<font color=red>嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间</font>**。这能够通过查看函数的func_closure属性得出结论，这个属性里面包含封闭作用域里面的值（*<font color=yellow>只会包含被捕捉到的值(???什么事被捕捉到的值)，比如x，如果在outer里面还定义了其他的值，封闭作用域里面是不会有的</font>*)

```python
def outer(x):
     def inner():
         print x 		# 1
     return inner
print1 = outer(1)
print2 = outer(2)
# ----------------------------------
print1()
1
print2()
2
```

从这个例子中你能够看到闭包(<u>被函数记住的封闭作用域</u>)能够被用来创建自定义的函数

## 装饰器  

装饰器其实就是一个闭包，把一个函数当做参数(*<font color=green>即上文的x</font>*)然后返回一个替代版函数

```python
def outer(some_func):
    def inner():
        print "before some_func"
        ret = some_func()					# 1
        return ret + 1
    return inner
def foo():
    return 1
decorated = outer(foo)						# 2
decorated()
before some_func
2
```


