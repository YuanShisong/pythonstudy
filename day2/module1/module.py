import sys
import os

# print(sys.path)
# print(sys.argv)  # python module.py 1 2 3 结果: ['module.py', '1', '2', '3']
# print(sys.argv[1])  # python module.py 1 2 3 结果: '1'

# print(sys.api_version)
# print(sys.version_info)
# print(sys.hash_info)

result1 = os.system("dir")  # 在操作系统上执行dir命令
print(result1, 'result1')

result2 = os.popen("dir").read()
print(result2)
