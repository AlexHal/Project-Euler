element = []
import time
start_time=time.time()
for i in range(1, 1000):
    if (i/3).is_integer():
        element.append(i)
    if (i/5).is_integer() and not (i/3).is_integer():
        element.append(i)
a = 0
for i in element:
    a= a + i
print(a)
endtime=time.time()
print(f"This took {start_time-endtime} seconds")
