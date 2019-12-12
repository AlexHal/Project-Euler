import time
start_time=time.time()
listg = []
numbers = []
m = 1
for i in range(101, 999):
    for k in range(101, 999):
        test = i*k
        numbers = [int(d) for d in str(test)]
        if numbers[0]==numbers[-1]:
            if numbers[1]==numbers[-2]:
                if numbers[2]==numbers[-3]:
                    result = test

                    if test >= m:
                        m=result
print(m)
endtime=time.time()
print(f"This took {abs(start_time-endtime)} seconds")
