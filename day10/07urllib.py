<<<<<<< HEAD
=======

>>>>>>> 54da3e9ef366ae21d6cb7ee9c9e8a8a8e31f157a
# 简单爬虫

import urllib, gevent
from urllib import request


def f(url):
<<<<<<< HEAD
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
=======
    print('GET: %s' %url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' %(len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org'),
    gevent.spawn(f, 'https://www.yahoo.com'),
    gevent.spawn(f, 'https://www.github.com')
])
>>>>>>> 54da3e9ef366ae21d6cb7ee9c9e8a8a8e31f157a
