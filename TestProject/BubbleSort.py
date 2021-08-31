# 冒泡排序--原创
import numpy as np
import datetime

listNum = np.random.randint(100, size=100)
print('原随机数组：')
print(listNum)

dtStart = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('算法开始时间' + dtStart)
for i in range(len(listNum)):
    for p in range(0, len(listNum) - i - 1):
        if listNum[p + 1] < listNum[p]:
            z = listNum[p + 1]
            listNum[p + 1] = listNum[p]
            listNum[p] = z
        else:
            pass
dtStop = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('算法结束时间' + dtStop)
print('排序后数组：')
print(listNum)
