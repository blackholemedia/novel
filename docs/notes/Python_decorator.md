
Table of Contents
=================

   * [Decorator](#decorator)
      * [阅读说明](#阅读说明)
      * [basic conception](#basic-conception)
      * [decorator](#decorator-1)
      * [被装饰函数带参数](#被装饰函数带参数)
      * [装饰函数带参数](#装饰函数带参数)
      * [functools.wraps](#functoolswraps)
      * [summary](#summary)

Created by ALTA
# Decorator  
## 阅读说明  

*<font color=#008000>绿色斜体</font>*代表个人的思考理解，*<font color=Yellow>黄色斜体</font>*代表阅读理解过程中的疑问，<font color=Red>红色正体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息`阴影`或 *一般斜体* 均表示引用或强调 

## basic conception  

动态添加函数功能的函数

```python
import time
def show_time(func):
    print("Begin:", time.ctime())
    func()
    print("End", time.ctime())

def bar():
    print("I am bar")

show_time(bar)
```

上述函数可以实现给任意函数增加打印运行前后时间的功能，但是会改变原有代码的运行逻辑(原来调用bar，现在调用show_time)

## decorator  

令bar 等于show_time(bar) ，就不需要改动以前的代码了(避免破坏原有代码逻辑)。所以，我们需要show_time(bar)返回一个函数对象，而这个函数对象内则是核心业务函数:func()与装饰函数：两个时间函数。

```python
import time
def show_time(func):
    def wrapper():
        print("Begin:", time.ctime())
        func()
        print("End", time.ctime())
    return wrapper

def bar():
    print("I am bar")

bar = show_time(bar)
bar()
```

@符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作

```python
@showtime   # bar = show_time(bar)
def bar():
    print('I am bar')
```



## 被装饰函数带参数  

被装饰的功能函数带有参数时，只需在wrapper()内对应加上参数即可

```python
import time

def show_time(func):
    def wrapper(a, b):
        print("Begin:", time.ctime())
        func(a, b)
        print("End:", time.ctime())
    return wrapper

@show_time 
def add(a, b):
    print(a+b)
```

## 装饰函数带参数  

上面的装饰器调用中，比如`@show_time`，该装饰器唯一的参数就是执行业务的函数。装饰器的语法允许我们在调用时，提供其它参数.**需要增加一层函数，给装饰函数创建一个新堆栈，装饰函数的参数的作用域即为此堆栈**

```python
def cal_time(flag):
    def show_time(func):
        def wrapper(a, b):
            start = time.ctime()
            print("Begin:", start)
            func(a, b)
            end = time.ctime()
            print("End:", end)
            if flag:
                print("Expend time:", time.mktime(time.strptime(end))-time.mktime(time.strptime(start)))
        return wrapper 
    return show_time

@cal_time(True)
def add(a, b):
    c = a + b
    time.sleep(1)
    print(c)

add(1, 2)
```

上面的`cal_time`是允许带参数的装饰器。它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。我们可以将它理解为一个含有参数的闭包。当我 们使用`@cal_time("true")`调用的时候，`Python`能够发现这一层的封装，并把参数传递到装饰器的环境中

## functools.wraps  

装饰器的一个缺点就是原函数的元信息不见了，比如函数的`docstring`、`__name__`、参数列表

```python
def foo():
    print('foo')

print(foo.__name__)

def logged(func):
    def wrapper(*args, **kwars):
        print(func.__name__ + 'was called')
        return func(*args, **kwargs)
    return wrapper

@logged
def bar(x):
    return x + x * x

print(bar.__name__)
# ---------------------------------- 输出结果
foo
wrapper
```

函数bar被wrapper取代了，于是其docstring，`__name__`就变成了wrapper函数的信息了。 这个问题可能引起一定的麻烦，好在我们有functools.wraps，**wraps本身也是一个装饰器，它能把原函数的元信息拷贝到装饰器函数中**，这使得装饰器函数也有和原函数一样的元信息

```python
from functools import wraps
def foo():
    print('foo')

print(foo.__name__)

def logged(func):
    @wraps(func)  # 只需加上这一句
    def wrapper(*args, **kwars):
        print(func.__name__ + 'was called')
        return func(*args, **kwargs)
    return wrapper

@logged
def bar(x):
    return x + x * x

print(bar.__name__)

# ---------------------------------- 输出结果
foo
bar
```

## summary  

- 装饰器就是为方便地为多个原函数创造其替代函数，该替代函数增加了一些额外功能
- 装饰器的基本结构是返回一个函数对象，该函数对象内包含：核心业务函数+装饰函数
- 如果核心业务函数带参数，则装饰器内定义“返回的函数对象”的时候也带上参数
- 如果装饰器要带参数，则在原装饰器上加一层函数，该函数带装饰器的参数即可
- 在装饰器内定义“返回的函数对象”之前加一句`functools.wraps`，即可将原函数的信息复制到装饰器函数
- 至于装饰器和闭包是什么毛线关系，参考