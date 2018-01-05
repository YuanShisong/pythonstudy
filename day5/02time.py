
# time标准库
import time  # 引入标准库
# 三种时间格式：时间戳，标准字符串格式，元组格式

# 1、元组格式和时间戳格式转换
# 获取时间戳
# >>> time.time()
# 1511950724.527984
# >>>

# 获取元组格式
# >>> time.gmtime()
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=29, tm_hour=10, tm_min=2, tm_sec=9, tm_wday=2, tm_yday=33
# 3, tm_isdst=0)
# >>> time.localtime()
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=29, tm_hour=18, tm_min=3, tm_sec=2, tm_wday=2, tm_yday=33
# 3, tm_isdst=0)

# 时间戳转为元组
# >>> time.localtime(1511950724.527984)
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=29, tm_hour=18, tm_min=18, tm_sec=44, tm_wday=2, tm_yday=
# 333, tm_isdst=0)
# >>>

# 元组转时间戳
# >>> x = time.localtime()
# >>> x
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=29, tm_hour=18, tm_min=20, tm_sec=31, tm_wday=2, tm_yday=
# 333, tm_isdst=0)
# >>> time.mktime(x)
# 1511950831.0
# >>>


# 元组格式和字符串格式
# 元组转字符串
# >>> time.strftime('%Y-%m-%d %H:%M:%S')
# '2017-11-29 18:14:57'
# >>>
# >>> x
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=29, tm_hour=18, tm_min=20, tm_sec=31, tm_wday=2, tm_yday=
# 333, tm_isdst=0)
# >>> time.strftime('%Y-%m-%d %H:%M:%S',x)
# '2017-11-29 18:20:31'
# >>>


# 字符串转元组
# >>> time.strptime('2017-11-29 18:14:57','%Y-%m-%d %H:%M:%S')
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=29, tm_hour=18, tm_min=14, tm_sec=57, tm_wday=2, tm_yday=
# 333, tm_isdst=-1)
# >>>

# datetime

import datetime
# >>> print(datetime.datetime.now())
# 2017-11-29 18:37:15.618534
# >>>

# 加3天
# >>> print(datetime.datetime.now() + datetime.timedelta(3))
# 2017-12-02 18:37:58.142966
# >>>

# 减3天
# >>> print(datetime.datetime.now() + datetime.timedelta(-3))
# 2017-11-26 18:38:45.691686
# >>>





