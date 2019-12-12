import time
start_time=time.time()
q=0
p=0
for i in range(0,101):
    q += i*i
    p += i

v = q-p*p
print(v)
endtime=time.time()
print(f"This took {abs(start_time-endtime)} seconds")
