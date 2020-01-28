
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# Linux学习笔记  
## 阅读说明  

*<font color=#008000>绿色斜体</font>*代表个人的思考理解，*<font color=Yellow>黄色斜体</font>*代表阅读理解过程中的疑问，<font color=Red>红色正体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```



### 

Content 

1. Number-prefix class  

   Content 

   - Symbol-prefix class 

     Content 

## Linux帮助命令  

### 帮助文档基本说明  

1. [] 可选内容  

2. <> 必选内容

3. a | b 二选一

4. { } 分组

5. ... 同一内容可出现多次

### whatis  

输入“whatis echo”，会显示如下信息。每行包含三部分，第一部分是命令名称；第二部分是命令在man手册出现的位置，第三部分是简述命令或函数的作用

```shell
>>>whatis echo
>>>echo (1) - display a line of text
```

如果想详细了解命令信息，可以输入如下命令：

```shell
>>>man 1 echo 或者 man echo(仅当数字为1时候可省略，其他数字不可省略)
```

### 内部命令（builtin）与外部命令  

man bash：   NAME字段后面的命令都是内部命令

### 查看内部命令使用方法  

1. help COMMAND  显示COMMAND这个命令的用法
2. man help 显示所有内部命令列表及使用方法

### 查看外部命令使用方法  

1. COMMAND  --help

```shell
>>>bash –-help  //部分命令，也可以简写为COMMAND -h
```

2. man COMMAND  原始格式为：man [章节] COMMAND，默认第1章省略  
3. info COMMAND

### man中的字段说明  

1. NAME 名称及简要说明

2. SYNOPSIS 用法格式说明

   - 可选内容

   - 必选内容

   - a|b 二选一

   - { } 分组

   - ... 同一内容可出现多次

3. DESCRIPTION 详细说明

4. OPTIONS 选项说明

5. EXAMPLES 示例

6. FILES 相关文件

7. AUTHOR 作者

8. COPYRIGHT 版本信息

9. REPORTING BUGS bug信息

10. SEE ALSO 其它帮助参考

### man手册查看命令  

- q Q ZZ 退出
- g  1g               光标跳至文档首部
- G         光标跳至文档尾部
- e j       文档前进N行
- y k      文档后退N行
- f space 文档前进N页
- b ^B    文档后退N页
-  /pattern n/N 向后查询
-  ?pattern        向前查询
- &pattern     只显示匹配到的行

### man手册章节  



   - Symbol-prefix class
   - 