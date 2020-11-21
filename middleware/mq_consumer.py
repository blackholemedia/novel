import sys
import os
import time
from random import uniform

import pika


class Consumer(object):

    def __init__(self):
        self.user = 'aqumon'
        self.pw = 'aqumon2046'
        self.connection = self.get_connection()
        self.channel = self.connection.channel()  # 获得channel

    def get_connection(self, host='192.168.200.27'):
        # endpoint = 'amqp://aqumon:aqumon2046@192.168.200.27:5762/%2F'
        credentials = pika.PlainCredentials(self.user, self.pw)
        parameters = pika.ConnectionParameters(host=host, credentials=credentials)
        return pika.BlockingConnection(parameters)  # 连接本地的RabbitMQ服务器

    def call_back(self, ch, method, properties, body):
        sleep_time = uniform(0.8, 5.4)
        print(" [x] Received %r time: %f" % (body, sleep_time))
        time.sleep(sleep_time)

    def consume_message(self):
        self.channel.queue_declare(queue='hello')  # 在RabbitMQ中创建hello这个队列
        self.channel.basic_consume(queue='hello',
                                   auto_ack=True,
                                   on_message_callback=self.call_back)  # 消息内容
        self.channel.start_consuming()

    def consume_by_exchange(self):
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.channel.queue_bind(exchange='logs',
                                queue=result.method.queue)
        self.channel.basic_consume(queue=result.method.queue,
                                   auto_ack=True,
                                   on_message_callback=self.call_back)  # 消息内容
        self.channel.start_consuming()

    def consume_by_key(self, i):
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.channel.queue_bind(exchange='direct_logs',
                                queue=result.method.queue,
                                routing_key=i)
        self.channel.basic_consume(queue=result.method.queue,
                                   auto_ack=True,
                                   on_message_callback=self.call_back)  # 消息内容
        self.channel.start_consuming()


if __name__ == '__main__':
    try:
        severity = sys.argv[1] if len(sys.argv) > 1 else '0'
        consumer = Consumer()
        # consumer.consume_message()
        # consumer.consume_by_exchange()
        consumer.consume_by_key(severity)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except Exception as ex:
        print(ex)
