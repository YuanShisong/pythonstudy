
# 断言：断言正确就继续向下走，断言错误则停止

a = 'hello'

assert a is 'hello'
print('ok')
assert type(a) is int  # AssertionError
print('It really i s str type.')

if __debug__:
    if not expression: raise AssertionError