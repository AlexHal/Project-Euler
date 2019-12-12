def seive(uper_bound):
    primes=[]
    nonprime=set()
    for i in range(2,uper_bound):
        if i not in nonprime:
            nonprime.update(range(i, uper_bound+1,i))
            primes.append(i)
    return primes
primes=seive(10000)

for prime in primes:
    for k in range(2,3500,2):
        if prime>1000 and prime+k in primes and prime+2*k in primes:
            #print(prime, prime+k, prime+2*k)
            first = set([int(d) for d in str(prime)])
            second =  set([int(d) for d in str(prime+k)])
            third =  set([int(d) for d in str(prime+2*k)])
            if first==second and second==third:
                print(prime, prime+k, prime+2*k)
