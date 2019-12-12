import time
start_time=time.time()
factors=[i for i in range(2,19)]
for i in range(116396280, 2793510720):
    if all(i%x==0 for x in factors):
        print(i)
        break
endtime=time.time()
print(f"This took {abs(start_time-endtime)} seconds")
