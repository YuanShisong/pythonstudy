#direct 类型 接收端
#思路：
#	1/ 声明exchange 名称和类型(direct)
#	2/ 指定接收级别
#	3/ 通过接收级别匹配发送的信息,routing_key

import pika, sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
	exchange_type='direct'
)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severties = sys.argv[1:]
print(severties)
if not severties:
	sys.stderr.write('Usage: %s [info] [warning] [error]\n' % sys.argv[0])
	sys.exit(1)

for severity in severties:
	channel.queue_bind(exchange='direct_logs',
		queue=queue_name,
		routing_key=severity
	)

print('[*] Waiting for logs. To exit press Ctrl+C')

def callback(ch, method, properties, body):
	print('[x] %r:%r' % (method.routing_key, body))

channel.basic_consume(callback,
	queue=queue_name,
	no_ack=1
)

channel.start_consuming()
