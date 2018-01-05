
# hashlib 模块 3.x中hashlib代替了md5,sha模块

import hashlib
m = hashlib.md5()
m.update(b'Hello')
print(m.hexdigest())
m.update(b'it is me')
print(m.hexdigest())

m.update(b'It"s been a long time since we spoken')
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b'Helloit is meIt"s been a long time since we spoken')
print(m2.hexdigest())