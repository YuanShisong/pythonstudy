# 消费者 即接收端
import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
chan = connection.channel()
chan.queue_declare(queue='hello_queue')

def callback(ch, method, properties, body):
	#print(ch, method, properties, body)
	time.sleep(6)
	print('[x] received %r' %body)

chan.basic_consume(callback,
	queue='hello_queue',
	no_ack=False  # no acknowledgement
)

print('[x] waiting for messages. To exit press Ctrl+C')
chan.start_consuming()
