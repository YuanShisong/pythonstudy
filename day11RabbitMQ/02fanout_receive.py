#广播 receive端

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明exchange 名称和类型
channel.exchange_declare(exchange='logs',
	exchange_type='fanout'	
)

result = channel.queue_declare(exclusive=True)  # 获取queue once we disconnect the consumer the queue should be deleted. There's an exclusive flag for that
queue_name = result.method.queue  # 获取queue的随机名

channel.queue_bind(exchange='logs',
	queue=queue_name
)

print('[*] Waiting for logs. To exit press Ctrl+C')

def callback(ch, method, properties, body):
	print('[X] %r' % body)

channel.basic_consume(callback,
	queue=queue_name,
	no_ack=True
)

channel.start_consuming()
