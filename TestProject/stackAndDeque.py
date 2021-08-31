#  队列和栈
from collections import deque


a = deque([[1, 'a'], [2, 'b'], [3, 'c']])
a.popleft()
a.append([3, 'nhn'])
print(a)
