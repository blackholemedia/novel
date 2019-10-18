1.  类的继承：

继承关系：继承是相对两个类而言的父子关系，子类继承了父类的所有**公有属性和方法**，继承实现了代码重用。

1.  **使用继承**

<!-- -->

1.  class Myclass(ParentClass)

如果父类定义了init方法，子类必须显式调用父类的init方法：

2.  ParentClass.init(self,\[args...\])

如果子类需要扩展父类的行为，可以添加init方法的参数

2.  **多重继承**

-   语法：

class class\_name(Parent\_c1,Parent\_c2,....)

-   注意：

当父类中出现多个自定义的init方法时，多重继承只执行第一个类的init方法，其它不执行。

1.  class People(object):

<!-- -->

3.  color = \'yellow\'

4.  5.  \# def \_\_init\_\_(self,
    c):\#参数大于等于2个，子类必须显式调用；只有一个参数的话，可以直接调用。单一继承

6.  def \_\_init\_\_(self):\#多重继承

7.  print \"Init\...\"

8.  self.dwell = \'Earth\'

9.  self.color = \'yellow\'

10. 11. def think(self):

12. print \"I am a %s\" %self.color

13. print \"My home is %s\" %self.dwell

14. print \"I am a thinker\"

15. 16. class Martian(object):

17. color = \'red\'

18. 19. def \_\_init\_\_(self):

20. self.dwell = \'Martian\'

21. 22. class Chinese(Martian, People):
    \#多重调用跟位置关系有关；可通过显式调用改变

23. def \_\_init\_\_(self):

24. \# People.\_\_init\_\_(self, \'red\')

25. People.\_\_init\_\_(self)

26. \# super(Chinese, self).\_\_init\_\_( \'red\')
    \#通过super函数继承父类

27. \# pass

28. \# def talk(self):

29. \# print(\"I like talking\")

30. \# def think(self): \#这里通过子类对父类的重写

31. \# print(\"I like talking\")

32. 33. cn = Chinese()

34. \# print cn.color \#继承父类的color

35. cn.think()

36. \# cn.talk()

<!-- -->

2.  类的属性-总结

-   类的属性，也有公有属性

-   类的私有属性

-   对象的公有属性

-   对象的私有属性

-   内置属性

-   函数的局部变量

1.  class MyClass(object):

<!-- -->

37. var1 = \'类属性，类的公有属性 var1\'

38. \_\_var2 = \'类的私有属性 \_\_var2\'

39. 40. def func1(self):

41. self.var3 = \'对象的公有属性 var3\' \#对象属性，只能对象访问

42. self.\_\_var4 = \'对象的私有属性 \_\_var4\'
    \#无法通过对象访问，类的外面

43. var5 = \'函数的局部变量 var5\' \#只能在函数的内部访问

44. print self.\_\_var4

45. print var5

46. 47. def func2(self):

48. print self.var1

49. print self.\_\_var2

50. print self.var3

51. print self.\_\_var4

52. 53. mc = MyClass()

54. mc.func1()

55. print(\'\*\*\*\*\*\*\' \* 10)

56. mc.func2()

57. print(\'\*\*\*\*\*\*\' \* 10)

58. print mc.\_\_dict\_\_

59. print MyClass.\_\_dict\_\_

60. \# \# print mc.var1 \#公有属性

61. \# \# print mc.\_MyClass\_\_var2 \#私有属性

62. \# \# print mc.var3

<!-- -->

3.  类的方法-总结

-   公有方法

-   私有方法

-   类方法

-   静态方法

-   内置方法

1.  class MyClass(object):

<!-- -->

63. name = \'Test\'

64. 65. def \_\_init\_\_(self):
    \#只需进行类的实例化，即可被调用。其它可不用

66. self.func1()

67. self.\_\_func2()

68. self.classFun()

69. self.staticFun()

70. 71. def func1(self):

72. print self.name,

73. print \"我是公有方法\"

74. \# self.\_\_func2() \#私有方法需通过内部调用，的方式间接调用

75. 76. def \_\_func2(self):

77. print self.name,

78. print \"我是私有方法\"

79. 80. *\@classmethod*

81. def classFun(self):

82. print self.name,

83. print \"我是类方法\"

84. 85. *\@staticmethod*

86. def staticFun():

87. print MyClass.name,

88. print \"我是静态方法\"

89. 90. mc = MyClass()

91. \# mc.func1()

92. \# MyClass.classFun()

93. \# MyClass.staticFun()
