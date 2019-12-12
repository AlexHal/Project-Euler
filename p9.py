import time
start_time=time.time()
import math
for a in range(0,1000):
    for b in range(a,1000):
        csquared = a*a+b*b
        c = math.sqrt(csquared)
        if (c).is_integer():
            if c>b:
                total=a+b+c
                if total==1000:
                    print(f"a={a}, b={b}, c={c}")
                    print(a*b*c)
endtime=time.time()
print(f"This took {abs(start_time-endtime)} seconds")
