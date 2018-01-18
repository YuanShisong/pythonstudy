import urllib.request


# url = 'http://word.iciba.com/?action=words&class=14&course=15'
#
# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)
#
# data = response.read()
#
# # 设置解码方式
# data = data.decode('utf-8')
#
# # 打印结果
# print(data)
#
# # 打印爬取网页的各类信息
#
# print(type(response))
# print(response.geturl())
# print(response.info())
# print(response.getcode())


# # 爬mp3
# url = "ed2k://|file|Le%20papillon.%E8%9D%B4%E8%9D%B6.2002.%E4%B8%AD%E6%96%87%E5%AD%97%E5%B9%95.1024x568.AVC-BaDao(ED2000.COM).mkv|794758384|C358D732DECF583AA14FA05ED907BF45|h=5GSGUYXWHPUA46NWLS5O7GKHYVOACMFC|/"
# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)
#
# data = response.read()
#
# print(len(data))
# 打印结果
# print(data)
# file = open('python-2.7.14.amd64.msi', 'bw')
# file.write(data)
# file.close()

import requests, time

start = time.time()
# url = 'ed2k://|file|Le%20papillon.%E8%9D%B4%E8%9D%B6.2002.%E4%B8%AD%E6%96%87%E5%AD%97%E5%B9%95.1024x568.AVC-BaDao(ED2000.COM).mkv|794758384|C358D732DECF583AA14FA05ED907BF45|h=5GSGUYXWHPUA46NWLS5O7GKHYVOACMFC|/'
# r = requests.get(url, stream=True)
# print(len(r))
# file = open('D:\\999-Personal\\99-电影\\蝴蝶python下载.mkv', 'bw')
# for chunk in r.iter_content(chunk_size=1024):
#     if chunk:
#         file.write(chunk)
# file.close()
end = time.time()
print('耗时:%s' % (end - start))
