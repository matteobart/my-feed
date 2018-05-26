import heapq
import datetime
m1 = datetime.date(1943,3, 13)  #year, month, day
m2 = datetime.date(1321,12,12)
m3 = datetime.date(2001, 12, 31)
m4 = datetime.date(2004, 1, 1)
h = []
heapq.heappush(h, (m1, 'write code'))
heapq.heappush(h, (m2, 'release product'))
heapq.heappush(h, (m3, 'write spec'))
heapq.heappush(h, (m4, 'create tests'))
print(h)