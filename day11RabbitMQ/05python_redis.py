# redis API练习
import redis

r = redis.Redis(host='localhost', port=6379)
r.set('foo', 'bar')
print(r.get('foo').decode())
