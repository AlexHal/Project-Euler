import time
start_time=time.time()
sum=0
primes=[]
prime_multiples = set()
for i in range(2, 2000000):
    if i not in prime_multiples:
        primes.append(i)
        prime_multiples.update(range(i, 2000000, i))

for prime in primes:
    sum+=prime
print(sum)
endtime=time.time()
print(f"This took {abs(start_time-endtime)} seconds")
