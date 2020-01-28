# 1.列表生成式
&emsp;&emsp; <font size=5>`L = ['Java' , 'C' , 'Swift' , 'Python' , 123]` ， 现在有 list 中包含字符串，和整数，把list中得大写字符转为小写，推到出另外一个list</font>

```python
R = [x.lower if isinstance(x.str) else x for x in L]
```

# 2.生成器(generator)杨辉三角<br>
&emsp;&emsp; <font size=5>生成器的关键就是如何根据生成器的程序执行特点定义函数内的循环体：</font>

```python
def triangle(max):
    n = 0
    l = [1]
    while n < max:
        yield l 
        if len(l) == 1:
            l.append(1)
        else:
            l = [1 if i == 0 else l[i]+l[i-1] for i in range(len(l))]
            l.append(1)
        #print(l)
        n = n + 1
    return 'done'

for x in triangle(10):
    print(x)
```

# 3.内部变量与private变量(此处变量即属性)
&emsp;&emsp; <font size=5>属性的名称前加上两个下划线`_`，就变成了一个私有变量（private）</font><br>&emsp;&emsp; <font size=5>变量名类似`__xxx__`的，以双下划线开头，以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量</font><br>&emsp;&emsp; <font size=5>一个下划线开头的实例变量名，比如`_name`，这样的实例变量外部可以访问，但按照约定俗成“请视为私有变量，不要随意访问”</font>

# 4.程序入口
&emsp;&emsp; <font size=5>`if __name__ == '__main__'`的意思是：当.py文件被直接运行时，`if __name__ == '__main__'`之下的代码块将被运行；当.py文件以模块形式被导入时，`if __name__ == '__main__'`之下的代码块不被运行</font>

# 5.super()函数/方法
&emsp;&emsp; <font size=5>super() 函数是用于调用父类(超类)的一个方法。单继承：super 与直接用类名调用父类方法无异；多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等问题，此时应区分super与直接类名调用父类</font><br>&emsp;&emsp; <font size=5>MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表(见附录 [1.方法解析顺序（Method Resolution Order, MRO）列表](#ap1))</font>

# 6.查找模块下的方法(函数)、属性
&emsp;&emsp; <font size=5> 均在python解释器下查询，详见附录 [2.查询模块的帮助文档](#ap2)</font>

# 7.Python时间格式化输出

&emsp;&emsp; <font size=5> `strftime()` 函数接收以时间元组(struct_time对象)，并返回以可读字符串表示的当地时间，格式由参数format决定</font>

```python
t = time.time()//获得以秒为单位的时间
print (time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))//gmtime获得struct_time对象
```
&emsp;&emsp; <font size=5> 格式参数format，详见附录 [3.python中时间日期格式化符号](#ap3)</font>

# 8.格式化输出

&emsp;&emsp; <font size=5> 格式输出详见参考文档 [python的格式化输出](file:///C:/Users/Alta/Desktop/编程笔记/python的格式化输出.pdf)</font>

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