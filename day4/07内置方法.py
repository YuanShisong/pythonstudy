
#

# all()  # 可迭代列表中是否都为真
# any()  # 可迭代列表中是否至少有一个为真
# print(ascii(1))
# print(bin(123))
# print(callable(1))  # 是否可调用
# print(chr(97))  # a
# print(ord('b'))  # 98

# compile() 将字符串编译成可执行的代码
code = 'for i in range(5):print(i)'
c = compile(code, '', 'exec')  # ValueError: compile() mode must be 'exec', 'eval' or 'single'
exec(c)

# c = compile(code, '', 'run')  # ValueError: compile() mode must be 'exec', 'eval' or 'single'
# run(c)
#
# c = compile(code, '', 'eval')  # ValueError: compile() mode must be 'exec', 'eval' or 'single'
# eval(c)
#
# c = compile(code, '', 'single')  # ValueError: compile() mode must be 'exec', 'eval' or 'single'
# exec(c)
