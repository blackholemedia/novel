
Table of Contents
=================

   * [Django URL](#django-url)
      * [阅读说明](#阅读说明)
      * [Django处理请求的过程](#django处理请求的过程)
      * [若干主要方法](#若干主要方法)
         * [path()/re_path()](#pathre_path)
         * [url()](#url)
         * [reverse()](#reverse)
         * [get_urls()](#get_urls)

Created by ALTA
# Django URL  

*<font color=#008000>绿色斜体</font>*代表个人的思考理解，*<font color=Yellow>黄色斜体</font>*代表阅读理解过程中的疑问，<font color=Red>红色正体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

参考链接: [reversing-admin-urls](<https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#reversing-admin-urls>) 

## Django处理请求的过程  

参考：[How Django processes a request](<https://docs.djangoproject.com/en/2.2/topics/http/urls/#how-django-processes-a-request>)  

1. Django决定使用的根URLconf模块， Django determines the root URLconf module to use. Ordinarily, this is the value of the [`ROOT_URLCONF`](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-ROOT_URLCONF) setting, but if the incoming `HttpRequest` object has a [`urlconf`](https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.HttpRequest.urlconf) attribute (set by middleware), its value will be used in place of the [`ROOT_URLCONF`](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-ROOT_URLCONF) setting
2. Django导入1中的Python模块并查找urlpatterns变量，Dango loads that Python module and looks for the variable `urlpatterns`. This should be a [sequence](https://docs.python.org/3/glossary.html#term-sequence) of [`django.urls.path()`](https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path) and/or [`django.urls.re_path()`](https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.re_path) instances
3. Django查找匹配请求的URL，Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL
4. 匹配成功则请求view函数，Once one of the URL patterns matches, Django imports and calls the given view, which is a simple Python function (or a [class-based view](https://docs.djangoproject.com/en/2.2/topics/class-based-views/)). The view gets passed the following arguments：
   - An instance of [`HttpRequest`](https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.HttpRequest)  
   - If the matched URL pattern returned no named groups, then the matches from the regular expression are provided as positional arguments
   - The keyword arguments are made up of any named parts matched by the path expression, overridden by any arguments specified in the optional `kwargs` argument to [`django.urls.path()`](https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path) or [`django.urls.re_path()`](https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.re_path).
5. 匹配失败则抛错误❎，If no URL pattern matches, or if an exception is raised during any point in this process, Django invokes an appropriate error-handling view. See [Error handling](https://docs.djangoproject.com/en/2.2/topics/http/urls/#error-handling) below

## 若干主要方法  

### path()/re_path()  

返回urlpatterns各个元素，Returns an element for inclusion in `urlpatterns`.参考：[path](<https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path>)

### url()  

This function is an alias to [`django.urls.re_path()`](https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.re_path). It’s likely to be deprecated in a future release.

### reverse()  

参考： [reverse](<https://docs.djangoproject.com/en/2.2/ref/urlresolvers/#reverse>) .通过view函数或是viewname返回url，例子如下：

```python
from news import views

path('archive/', views.archive, name='news-archive')
```

you can use any of the following to reverse the URL:

```python
# using the named URL
reverse('news-archive')

# passing a callable object
# (This is discouraged because you can't reverse namespaced views this way.)
from news import views
reverse(views.archive)
```

###  get_urls()  

ModelAdmin类下的一个方法，返回与URLconf一致的urls，即返回类似于urlpatterns的list. The `get_urls` method on a `ModelAdmin` returns the URLs to be used for that ModelAdmin in the same way as a URLconf. Therefore you can extend them as documented in [URL dispatcher](https://docs.djangoproject.com/en/2.2/topics/http/urls/)  

工作过程：Django在部署的时候即调用该方法([reversing-admin-urls](<https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#reversing-admin-urls>)， 对应源码admin/sites/AdminSite下的get_urls()方法)，保留着类似于urlpatterns的全局变量，因此调用path()定义urlpatterns中元素的时候，如果定义了同名的元素(即view或者viewname相同)，元素会被覆盖。实例请参考如下：