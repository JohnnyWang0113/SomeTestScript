# 直接插入排序--原创未完成
import numpy as np
import datetime

listNum = np.random.randint(100, size=100)
print('原随机数组：')
print(listNum)

dtStart = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('算法开始时间' + dtStart)

# ...

dtStop = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('算法结束时间' + dtStop)
print('排序后数组：')
print(listNum)


