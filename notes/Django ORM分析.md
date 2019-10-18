
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# template  
## 阅读说明  

*<font color=#008000>绿色斜体</font>*代表个人的思考理解，*<font color=Yellow>黄色斜体</font>*代表阅读理解过程中的疑问，<font color=Red>红色正体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

[参考资料](<https://www.jianshu.com/p/ac87788b55f3>)  


Content 

1. Number-prefix class  

   Content 

   - Symbol-prefix class 

     Content 

## manager  

### manager继承QuerySet所有方法  
modle.objects中的objects是modle的manager，manager是Manager类，俗称管理器，他是继承BaseManager并且通过BaseManager.get_queryset(QuerySet),将QuerySet类的所有方法都添加到了manager中，所以modle.objects.using(db).all()其实就是modle.objects.queryset.using(db).all()；  



### second-class title  

1. Number-prefix class  
   - Symbol-prefix class
   - 