
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# Yield  
## 阅读说明  

*<font color=#008000>绿色斜体</font>*代表个人的思考理解，*<font color=Yellow>黄色斜体</font>*代表阅读理解过程中的疑问，<font color=Red>红色正体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```



## 直观但不精确的理解  

### yield相当于return  

```python
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g)
# ---------------------------------- 输出结果
starting...
4
********************
res: None
4
```

1. 程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个对象
2. 直到调用next方法，foo函数正式开始执行，寻找遇到的第一个yield表达式
3. 程序遇到yield表达式，获得yield表达式返回值
4. 程序执行print("*"*20)，输出20个*
5. 从刚才那个next程序停止的地方开始执行的，也就是要执行res的赋值操作，这时候要注意，这个时候赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边传参数），所以这个时候res赋值是None,所以接着下面的输出就是res:None,
6. 程序会继续在while里执行，又一次碰到yield,这个时候同样return 出4，然后程序停止，print函数输出的4就是这次return出的4.

### send()和next()  

`send()`可以传递`yield`的值，`next()`只能传递`None`。所以`next()` 和 `send(None)`作用是一样的。

```python
def s():
    print('study yield')
    m = yield 5
    print(m)
    d = yield 16
    print('go on!')


c = s()
s_d = next(c)  # 相当于send(None)
c.send('Fighting!')

# ---------------------------------- 输出结果
study yield
Fighting!
```

### 对于原理的个人理解  

Yield表达式实质相当于一个中断操作：1. 先return yield后面的值，2. 然后中断等待着，直到有下一个值传进来再继续执行。如上述的`m = yield 5`, 调用send(None)(即next()), 先return yield 后面的5，然后中断等待着(即赋值操作一直在等待着)，直到下一次调用send(None)的时候继续执行程序(执行赋值)，此时发现send传入来的参数是None，所以将None赋值给m。不断以此类推。

## Yield from  

简单地说，yield from  generator 。实际上就是**返回另外一个生成器**， 生成器嵌套  

```python
def generator1():
    item = range(10)
    for i in item:
        yield i

def generator2():
    yield 'a'
    yield 'b'
    yield 'c'
    yield from generator1() #yield from iterable本质上等于 for item in iterable: yield item的缩写版
    yield from [11,22,33,44]
    yield from (12,23,34)
    yield from range(3)

for i in generator2() :
    print(i)
```

上述代码执行结果：

```python
a
b
c
0
1
2
3
4
5
6
7
8
9
11
22
33
44
12
23
34
0
1
2
```

