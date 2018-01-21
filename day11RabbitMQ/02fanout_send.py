# 广播

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#声明exchange
channel.exchange_declare(exchange='logs',
	exchange_type='fanout'  # 注册为fanout类型
)

message = ' '.join(sys.argv[1:]) or 'info:Hello World!'

channel.basic_publish(exchange='logs',
	routing_key='',  # 这次key为空
	body=message
)

print('[x] Sent %r' % message)
connection.close()
