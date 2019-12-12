import time
start_time=time.time()


def seive(uper_bound):
    primes=[]
    nonprime=set()
    for i in range(2,uper_bound):
        if i not in nonprime:
            nonprime.update(range(i, uper_bound+1,i))
            primes.append(i)
            if len(primes)==10002:
                break
    return primes
primes=seive(200000)
print(primes[10000])
endtime=time.time()
print(f"This took {abs(start_time-endtime)} seconds")
