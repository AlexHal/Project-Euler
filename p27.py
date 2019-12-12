
def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step
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
miow= sieve(20000)
countf=0
for a in range(-999, 1000):
    for b in range(0,1001):
        n=0
        for n in range(0,100):
            attempt=n*n+a*n+b
            if attempt in miow:
                n+=1
            else:
                break
        if n > countf:
            countf = n
            print(f"a={a} with b={b} gave {countf} consecutive primes with product {a*b}")
