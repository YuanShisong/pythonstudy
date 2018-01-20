# rabbitmq Hello World例子

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
chan = connection.channel()

#声明queue
chan.queue_declare(queue='hello_queue')

chan.basic_publish(exchange='',  # 
	routing_key='hello_queue',  # key
	body='Hello World!>>>>>>>>>>>>>'  # 内容
)

print('[x] Sent Hello World!')

connection.close()
