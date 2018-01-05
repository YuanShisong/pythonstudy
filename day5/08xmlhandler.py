
# python处理xml

import xml.etree.ElementTree as xee

tree = xee.parse('testxml.xml')
root = tree.getroot()
# print(root)
# print(root.tag)
# print(root.value)

# 遍历节点
# for child in root:
#     print(child.tag, child.attrib)
#     for cc in child:
#         print(cc.tag, cc.text)
#         # print(cc.tag, cc.attrib)

# for i in root.iter('task'):
#     print(i.text())

# 修改
# for i in root.iter('task'):
#     # print(i.text())
#     i.set('id', 'joshua')
#
# tree.write('testxml.xml')

# 删除节点
for i in root.iter('task'):
    root.remove(i)
tree.write('testxml.xml')