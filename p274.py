import time
start_time = time.time()
def candidate_range(n):
    cur = 5
    incr = 2
    while cur < n+1:
        yield cur
        cur += incr
        incr ^= 6 # or incr = 6-incr, or however
def sieve(end):
    prime_list = [2, 3]
    sieve_list = [True] * (end+1)
    for each_number in candidate_range(end):
        if sieve_list[each_number]:
            prime_list.append(each_number)
            for multiple in range(each_number*each_number, end+1, each_number):
                sieve_list[multiple] = False
    return prime_list
def inv(a,m):
    return 1 if a==1 else ((a-inv(m%a,a))*m+1)//a

coprimes=sieve(10**7)
coprimes.remove(2)
coprimes.remove(5)
sum=0
for prime in coprimes:
    sum= sum+inv(10, prime)
print(coprimes[-1], sum)
print("--- %s seconds ---" % (time.time() - start_time))
