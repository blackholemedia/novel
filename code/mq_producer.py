import pika


class Producer(object):

    def __init__(self):
        self.user = 'aqumon'
        self.pw = 'aqumon2046'

    def get_connection(self, host='192.168.200.27'):
        # endpoint = 'amqp://aqumon:aqumon2046@192.168.200.27:5762/%2F'
        credentials = pika.PlainCredentials(self.user, self.pw)
        parameters = pika.ConnectionParameters(host=host, credentials=credentials)
        return pika.BlockingConnection(parameters)  # 连接本地的RabbitMQ服务器

    def send_message(self):
        connection = self.get_connection()
        channel = connection.channel()  # 获得channel
        channel.queue_declare(queue='hello')  # 在RabbitMQ中创建hello这个队列
        channel.basic_publish(exchange='',  # 使用默认的exchange来发送消息到队列
                              routing_key='hello',  # 发送到该队列 hello 中
                              body='Hello World!')  # 消息内容
        connection.close()  # 关闭 同时flush


if __name__ == '__main__':
    producer = Producer()
    producer.send_message()
