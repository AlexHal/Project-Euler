import time
start_time=time.time()
def seive(uper_bound):
    primes=[]
    nonprime=set()
    for i in range(2,uper_bound):
        if i not in nonprime:
            nonprime.update(range(i, uper_bound+1,i))
            primes.append(i)
    return primes

primes=seive(75143)
final=[]
for i in primes:
    if 600851475143%i==0:
        final.append(i)
endtime=time.time()
print(final)
print(f"This took {abs(start_time-endtime)} seconds")
