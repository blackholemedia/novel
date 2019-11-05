
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# Rasa Core  
## 阅读说明  

*<font color=#008000>绿色斜体</font>*代表个人的思考理解，*<font color=Yellow>黄色斜体</font>*代表阅读理解过程中的疑问，<font color=Red>红色正体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考链接  

1. [Rasa Core开发指南](https://blog.csdn.net/AndrExpert/article/details/92805022)
2. [A Beginner’s Guide to Rasa NLU for Intent Classification and Named-entity Recognition](<https://towardsdatascience.com/a-beginners-guide-to-rasa-nlu-for-intent-classification-and-named-entity-recognition-a4f0f76b2a96>)
3. 

 ## 基本概念  

### Intent  

意图：An intent represents the purpose of a user's input. You define an intent for each type of user request you want your application to support  

### Entity  

实体：An entity represents a term or object that is relevant to your intents and that provides a specific context for an intent. You list the possible values for each entity and synonyms that users might enter

### Channel  



## Rasa结构及流程  

参考：[rasa对话系统解析系列](./rasa_details.md)

### 训练 

### 服务

1. 启动Rasa服务(启动一个HTTP服务， API[参考](<https://rasa.com/docs/rasa/api/http-api/#http-api>))
2. 

Rasa向action server发送包含执行哪个action信息`POST`请求([execute-actions-in-other-code](<https://rasa.com/docs/rasa/core/actions/#execute-actions-in-other-code>)），请求规范[参考](<https://rasa.com/docs/rasa/api/action-server/#action-server>)

## Rasa Core消息处理流程(slots的处理？)  

1. 将用户输入的Message传递到Interpreter(NLU模块)，该模块负责识别Message中的"意图(intent)“和提取所有"实体”(entity)数据；
2. Rasa Core会将Interpreter提取到的意图和识别传给Tracker对象，该对象的主要作用是跟踪会话状态(conversation state)；
3. 利用policy记录Tracker对象的当前状态，并选择执行相应的action，其中，这个action是被记录在Track对象中的；
4. 最后，将执行action返回的结果输出即完成一次人机交互

## Custom actions  

CustomAction，即自定义action，允许开发者执行任何操作并反馈给用户，比如简单的返回一串字符串，或者控制家电、检查银行账户余额等等。它与DefaultAction不同，**自定义action需要我们在domain.yml文件中的actions部分先进行定义，然后在指定的webserver中实现它，其中，这个webserver的url地址在endpoint.yml文件中指定**，并且这个webserver可以通过任何语言实现，当然这里首先推荐python来做，毕竟Rasa Core为我们封装好了一个rasa-core-sdk专门用来处理自定义action. custom actions在Rasa中的**使用方式并不是直接调用，而是采用服务的形式**，所以如果想使用自定义的action，还需要定义一个endpoints.yml文件，文件内容如下：

```python
action_endpoint:
  url: 'http://localhost:5055/webhook'
```

在启动会话的时候添加额外的命令--endpoints endpoints.yml，该命令会在5055端口启动一个服务，这个服务就是我们定义的action

## NLU training data format(markdown)  

训练数据包括以下类型：common examples，synonyms，regex features，lookup tables

```python
## intent:check_balance
- what is my balance <!-- no entity -->
- how much do I have on my [savings](source_account) <!-- entity "source_account" has value "savings" -->
- how much do I have on my [savings account](source_account:savings) <!-- synonyms, method 1-->
- Could I pay in [yen](currency)?  <!-- entity matched by lookup table -->

## intent:greet
- hey
- hello

## synonym:savings   <!-- synonyms, method 2 -->
- pink pig

## regex:zipcode
- [0-9]{5}

## lookup:currencies   <!-- lookup table list -->
- Yen
- USD
- Euro

## lookup:additional_currencies  <!-- no list to specify lookup table file -->
path/to/currencies.txt
```

### common examples - Intents  

starting with `##`, specify intent with ## intent:name_of_intent followed by a list of questions for the intent

```python
## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- talk to you later
```

### common examples - Entity  

specify the entity inside each of the question as follow `[value](name of entity)`

```python
## intent:ask_shop_open
- does the shop open on [monday](weekday)
- does the shop open on [wednesday](weekday)
- does the shop open on [friday](weekday)
```

### Lookup table  

a long list of values for a single entity

```python
## lookup:currencies   <!-- lookup table list -->
- Yen
- USD
- Euro

## lookup:countries  <!-- no list to specify lookup table file -->
path/to/countries.txt
"""
In the countries.txt, you can specify each of the element in a new line as follow
singapore
malaysia
vietnam
indonesia
thailand
"""
```

**you have to provide a few examples for it to generalize**

```python
## intent:inform_country_of_origin
- i am from [malaysia](countries)
- i am from [vietnam](countries)
- i came from [thailand](countries)
```

### Synonym  

identify synonym and map it back to a single value. The first method is to add it inline like `[synonym1](entity:value)`

```python
## intent:ask_eaten
- what did you have for [breakfast](meal)
- what did you have for [break fast](meal:breakfast)
- what did you have for [breakfat](meal:breakfast)
```

The second method is as follow：

```python
## synonym:breakfast
- brekfast
- brokefast
```

What makes synonym differs from lookup table is that **synonym will map the value of the entity to a single value (breakfast in this example)**. In other words, synonym is great for catching spelling mistakes and acronym while lookup table is great for generalizing the examples

### Regex  

```python
## intent:inform_zipcode
- my zipcode is [12345](zipcode)
- my zipcode is [33456](zipcode)
- my zipcode is [94056](zipcode)
## regex:zipcode
- [0-9]{5}
```

## Stories 

### Data format  

1. story title  

   仅仅起描述作用

2. user messages  

   starting with `*` in the format `intent{"entity1": "value", "entity2": "value"}`

3. action  

   starting with `-`

4. events  

   Events returned by an action are on lines immediately after that action. For example, if an action returns a `SlotSet` event, this is shown as `slot{"slot_name": "value"}`

## config.yaml  

### language  

语言

### pipeline  

组件

### policy  

Rasa-core使用的策略

## domain.yaml  

`机器的知识库`

### intents  
你期望用户说的东西
### entities  
您想要从消息中提取的信息片段。
### actions  
你的机器人可以做和说的东西
### slots  
在会话期间跟踪的信息（例如用户年龄）
### templates  
你的机器人可以说的东西的模板字符串

## Actions  

1. Utterance actions  

   start with `utter_` and send a specific message to the user





### second-class title  

1. Number-prefix class  
   - Symbol-prefix class
   - 