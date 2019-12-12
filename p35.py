import time
start_time = time.time()
def even(list1):
    list1=[int(n) for n in str(list1)]
    list2= [0,2,4,6,8]
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result
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
primes = sieve(10**6)
def rotation(number):
    return {int(str(number)[rot:] + str(number)[:rot]) for rot in range(len(str(number)))}
good = [3,7]
for prime in primes:
    if not even(prime) and rotation(prime).issubset(primes):
        for i in rotation(prime):
            good.append(i)
            primes.remove(i)
        print(prime, rotation(prime), len(good))
#the boy forgets 5 but wtv
