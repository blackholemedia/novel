
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# 请求过程  
## 阅读说明  

*<font color=#008000>绿色斜体</font>*代表个人的思考理解，*<font color=Yellow>黄色斜体</font>*代表阅读理解过程中的疑问，<font color=Red>红色正体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## server启动过程中的相关设置  

1. 根据参数—enable-api是否设置HTTP API 

   ```python
   # rasa/core/run.py
   if enable_api:				# 主要操作就是注册一组HTTP API
       app = server.create_app(
           cors_origins=cors,
           auth_token=auth_token,
           jwt_secret=jwt_secret,
           jwt_method=jwt_method,
           endpoints=endpoints,
       )
   else:
       app = _create_app_without_api(cors)
   if input_channels:		# 注册input_channel的API，即post请求的/webhooks/rest/webhook
       channels.channel.register(input_channels, app, route=route)
   ```

2. server启动前初始化一个agent实例

   ```python
   # rasa/core/run.py
   app.register_listener(
           partial(load_agent_on_start, model_path, endpoints, remote_storage),
           "before_server_start",
       )
   ```

   

##  请求过程  

正常状态处理

1. /webhooks/rest/webhook路由至receive方法， 异步调用on_new_message方法， on_new_message实质调用agent实例的handle_message方法

   ```python
   # rasa/core/channels/channel.py
   def register(
       input_channels: List["InputChannel"], app: Sanic, route: Optional[Text]
   ) -> None:
       async def handler(*args, **kwargs):
           await app.agent.handle_message(*args, **kwargs)
   				.
           .
           app.blueprint(channel.blueprint(handler), url_prefix=p)
   ```

   

   ```python
   # rasa/core/channels/channel.py
   def blueprint(
       self, on_new_message: Callable[[UserMessage], Awaitable[None]]
   ) -> Blueprint:
       custom_webhook = Blueprint(
           "custom_webhook_{}".format(type(self).__name__),
           inspect.getmodule(self).__name__,
       )
       .
       .
       @custom_webhook.route("/webhook", methods=["POST"])
           async def receive(request: Request) -> HTTPResponse:
           .
           .
           		try:
           		    await on_new_message(  # 同时将请求中的所有信息封装为UsewrMessage对象
           		        UserMessage(
           		            text,
           		            collector,
           		            sender_id,
           		            input_channel=input_channel,
           		            metadata=metadata,
           		        )
           		    )
           		except CancelledError:
   ```

2. 在agent的hand_message方法中，异步调用processor实例的handle_message方法

   ```python
   # rasa/core/agent.py
   async def handle_message(
           self,
           message: UserMessage,
           message_preprocessor: Optional[Callable[[Text], Text]] = None,
           **kwargs,
       ) -> Optional[List[Dict[Text, Any]]]:
     			.
     			.
           processor = self.create_processor(message_preprocessor)
           async with self.lock_store.lock(message.sender_id):
               return await processor.handle_message(message)
   ```

3. 在processor的hand_message方法中，异步调用`_predict_and_execute_next_action`方法，然后调用`_save_tracker`方法

   ```python
   # rasa/core/processor.py
   async def handle_message(
           self, message: UserMessage
       ) -> Optional[List[Dict[Text, Any]]]:
     			.
     			.
     			await self._predict_and_execute_next_action(message, tracker)
     			# save tracker state to continue conversation from this state
     			self._save_tracker(tracker)
```
   
   

### second-class title  

1. Number-prefix class  
   - Symbol-prefix class
   - 