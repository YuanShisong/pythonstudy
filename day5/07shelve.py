import shelve, datetime

s = shelve.open('shelvetest')
# name = ['zhangfei', 'guanyu', 'liubei']
# info = {'chaodai': 'sanguo', 'age': 1800}
# s['name'] = name
# s['info'] = info
# s['time'] = datetime.datetime.now()

print(s.get('info'))
print(s.get('info').get('chaodai'))
print(s.get('time'))
print(s.items())
for i in s.items():
    print(i)

s.close()
