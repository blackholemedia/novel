import pika


class Producer(object):

    def __init__(self):
        self.user = 'aqumon'
        self.pw = 'aqumon2046'
        self.connection = self.get_connection()

    def get_connection(self, host='192.168.200.27'):
        # endpoint = 'amqp://aqumon:aqumon2046@192.168.200.27:5762/%2F'
        credentials = pika.PlainCredentials(self.user, self.pw)
        parameters = pika.ConnectionParameters(host=host, credentials=credentials)
        return pika.BlockingConnection(parameters)  # 连接本地的RabbitMQ服务器

    def close_connection(self):
        self.connection.close()  # 关闭 同时flush

    def send_message(self):
        channel = self.connection.channel()  # 获得channel
        channel.queue_declare(queue='hello')  # 在RabbitMQ中创建hello这个队列
        for i in range(10):
            msg = 'The {} message'.format(str(i + 1))
            channel.basic_publish(exchange='',  # 使用默认的exchange来发送消息到队列
                                  routing_key='hello',
                                  body=msg)  # 消息内容


if __name__ == '__main__':
    producer = Producer()
    producer.send_message()
    producer.close_connection()
