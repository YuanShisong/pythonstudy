# 简单爬虫

import urllib, gevent
from urllib import request


def f(url):
	print('GET: %s' %url)
	resp = request.urlopen(url)
	data = resp.read()
	print(data)
	print('%d bytes received from %s.' %(len(data), url))


gevent.joinall([
	gevent.spawn(f, 'https://www.python.org'),
	gevent.spawn(f, 'https://www.yahoo.com'),
	gevent.spawn(f, 'https://www.github.com')
])
