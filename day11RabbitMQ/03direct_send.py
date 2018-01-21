# direct 方式广播 发送方
# 思路：1/ 声明exchange 名称和类型(direct)
#		2/ 发送消息时指定消息级别
#		3/ 将消息级别做索引key，即routing_key

import pika, sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
	exchange_type='direct'
)

severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
print(severity)
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='direct_logs',
	routing_key=severity,
	body=message
)

print('[x] Sent %r:%r' % (severity, message))

connection.close()
