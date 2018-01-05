
# 异常处理
list = []
dict = {}
try:
    list[1]
    dict['name']
except (KeyError, IndexError) as e:
    print('Error', e)

except Exception:
    print('未知错误')
else:  # 没有错误
    print('没有错误')
finally:  # 不管有没有错 都会执行
    print('finally')

print('after exception')


print('\n---------自定义异常---------')


class MyException(BaseException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise MyException('自定义异常')
except BaseException as e:
    print('Error', e)
