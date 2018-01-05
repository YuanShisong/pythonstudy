
# 写配置文件
import configparser
parser = configparser.ConfigParser()
# # 以json格式写
# parser['DEFAULT']={
#     'name':'Joshua',
#     'age':29,
#     'sex':'male',
#     'other':{
#         'hobby':['gym', 'marathon', 'photo'],
#         'height':175
#     }
# }
# # 逐层写
# parser['INFO'] = {}
# parser['INFO']['name'] = 'joshua'
# parser['INFO']['sex'] = 'male'
# parser['INFO']['age'] = '29'
# parser['HOBBY']={
#     'indoor':['gym', 'photo'],
#     'outdoor':['hiking', 'marathon']
# }
#
# with open('joshua.config', 'w') as configfile:
#     parser.write(configfile)

# 读配置文件
parser.read('joshua.config')
# print(parser.defaults())
# for i in parser.defaults():
#     print(i)
#
# print('/n-----------')
# print(parser.sections())
# for i in parser.sections():
#     print(i)

# print(parser['DEFAULT']['name'])
# print(parser['DEFAULT']['other'][0])  # 结果:"{" 第一个字符
# print(type(parser['DEFAULT']['other']))  # <class 'str'>

# 删除某一项配置 写入到新文件中
success = parser.remove_section('INFO')
# print(type(second))  # <class 'bool'>
if success:
    parser.write(open('josh.conf', 'w'))
