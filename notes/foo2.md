类的继承：

继承关系：继承是相对两个类而言的父子关系，子类继承了父类的所有__公有属性和方法__，继承实现了代码重用。

- 
	1. __使用继承__

class Myclass\(ParentClass\) 

如果父类定义了init方法，子类必须显式调用父类的init方法： 

ParentClass\.init\(self,\[args…\]\) 

如果子类需要扩展父类的行为，可以添加init方法的参数

- 
	1. __多重继承__
- 语法： 

class class\_name\(Parent\_c1,Parent\_c2,…\.\)

- 注意： 

当父类中出现多个自定义的init方法时，多重继承只执行第一个类的init方法，其它不执行。

1. class People\(object\):

    color = 'yellow'

    \# def \_\_init\_\_\(self, c\):\#参数大于等于2个，子类必须显式调用；只有一个参数的话，可以直接调用。单一继承

    def \_\_init\_\_\(self\):\#多重继承

        print "Init\.\.\."

        self\.dwell = 'Earth'

        self\.color = 'yellow'

    def think\(self\):

        print "I am a %s" %self\.color

        print "My home is %s" %self\.dwell

        print "I am a thinker"

class Martian\(object\):

    color = 'red'

    def \_\_init\_\_\(self\):

        self\.dwell = 'Martian'

class Chinese\(Martian, People\): \#多重调用跟位置关系有关；可通过显式调用改变

    def \_\_init\_\_\(self\):

        \# People\.\_\_init\_\_\(self, 'red'\)

        People\.\_\_init\_\_\(self\)

        \# super\(Chinese, self\)\.\_\_init\_\_\( 'red'\) \#通过super函数继承父类

    \# pass

    \# def talk\(self\):

    \#     print\("I like talking"\)

    \# def think\(self\): \#这里通过子类对父类的重写

    \#     print\("I like talking"\)

cn = Chinese\(\)

\# print cn\.color \#继承父类的color

cn\.think\(\)

\# cn\.talk\(\)

类的属性\-总结

- 类的属性，也有公有属性
- 类的私有属性
- 对象的公有属性
- 对象的私有属性
- 内置属性
- 函数的局部变量

1. class MyClass\(object\):

    var1 = '类属性，类的公有属性 var1'

    \_\_var2 = '类的私有属性 \_\_var2'

    def func1\(self\):

        self\.var3 = '对象的公有属性 var3'  \#对象属性，只能对象访问

        self\.\_\_var4 = '对象的私有属性 \_\_var4'  \#无法通过对象访问，类的外面

        var5 = '函数的局部变量 var5'  \#只能在函数的内部访问

        print self\.\_\_var4

        print var5

    def func2\(self\):

        print self\.var1

        print self\.\_\_var2

        print self\.var3

        print self\.\_\_var4

mc = MyClass\(\)

mc\.func1\(\)

print\('\*\*\*\*\*\*' \* 10\)

mc\.func2\(\)

print\('\*\*\*\*\*\*' \* 10\)

print mc\.\_\_dict\_\_

print MyClass\.\_\_dict\_\_

\# \# print mc\.var1  \#公有属性

\# \# print mc\.\_MyClass\_\_var2 \#私有属性

\# \# print mc\.var3

类的方法\-总结

- 公有方法
- 私有方法
- 类方法
- 静态方法
- 内置方法

1. class MyClass\(object\):

    name = 'Test'

    def \_\_init\_\_\(self\): \#只需进行类的实例化，即可被调用。其它可不用

        self\.func1\(\)

        self\.\_\_func2\(\)

        self\.classFun\(\)

        self\.staticFun\(\)

    def func1\(self\):

        print self\.name,

        print "我是公有方法"

        \# self\.\_\_func2\(\) \#私有方法需通过内部调用，的方式间接调用

    def \_\_func2\(self\):

        print self\.name,

        print "我是私有方法"

    *@classmethod*

    def classFun\(self\):

        print self\.name,

        print "我是类方法"

    *@staticmethod*

    def staticFun\(\):

        print MyClass\.name,

        print "我是静态方法"

mc = MyClass\(\)

\# mc\.func1\(\)

\# MyClass\.classFun\(\)

\# MyClass\.staticFun\(\)

