import sys
import os

import pika


class Consumer(object):

    def __init__(self):
        self.user = 'aqumon'
        self.pw = 'aqumon2046'

    def get_connection(self, host='192.168.200.27'):
        # endpoint = 'amqp://aqumon:aqumon2046@192.168.200.27:5762/%2F'
        credentials = pika.PlainCredentials(self.user, self.pw)
        parameters = pika.ConnectionParameters(host=host, credentials=credentials)
        return pika.BlockingConnection(parameters)  # 连接本地的RabbitMQ服务器

    def call_back(self, ch, method, properties, body):
        print(" [x] Received %r" % body)

    def consume_message(self):
        connection = self.get_connection()
        channel = connection.channel()  # 获得channel
        channel.queue_declare(queue='hello')  # 在RabbitMQ中创建hello这个队列
        channel.basic_consume(queue='hello',  # 使用默认的exchange来发送消息到队列
                              auto_ack=True,  # 发送到该队列 hello 中
                              on_message_callback=self.call_back)  # 消息内容
        channel.start_consuming()


if __name__ == '__main__':
    try:
        consumer = Consumer()
        consumer.consume_message()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
