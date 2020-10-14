import pika


class Producer(object):

    def __init__(self):
        self.user = 'aqumon'
        self.pw = 'aqumon2046'
        self.connection = self.get_connection()
        self.channel = self.connection.channel()  # 获得channel
        # self.exchange = self.channel.exchange_declare('logs', exchange_type='fanout')
        self.exchange = self.channel.exchange_declare('direct_logs', exchange_type='direct')

    def get_connection(self, host='192.168.200.27'):
        # endpoint = 'amqp://aqumon:aqumon2046@192.168.200.27:5762/%2F'
        credentials = pika.PlainCredentials(self.user, self.pw)
        parameters = pika.ConnectionParameters(host=host, credentials=credentials)
        return pika.BlockingConnection(parameters)  # 连接本地的RabbitMQ服务器

    def close_connection(self):
        self.connection.close()  # 关闭 同时flush

    def send_message(self):
        self.channel.queue_declare(queue='hello')  # 在RabbitMQ中创建hello这个队列
        for i in range(10):
            msg = 'The {} message'.format(str(i + 1))
            self.channel.basic_publish(exchange='',
                                       routing_key='hello',
                                       body=msg)

    def send_exchange(self):
        for i in range(100):
            msg = 'The {} message'.format(str(i + 1))
            self.channel.basic_publish(exchange='logs',
                                       routing_key='',
                                       body=msg)

    def send_by_key(self):
        for i in range(50):
            msg = 'The {} message'.format(str(i + 1))
            self.channel.basic_publish(exchange='direct_logs',
                                       routing_key=str(i % 3),
                                       body=msg)


if __name__ == '__main__':
    producer = Producer()
    # producer.send_message()
    # producer.send_exchange()
    producer.send_by_key()
    producer.close_connection()
