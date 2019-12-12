def seive(uper_bound):
    primes=[]
    nonprime=set()
    for i in range(2,uper_bound):
        if i not in nonprime:
            nonprime.update(range(i, uper_bound+1,i))
            primes.append(i)
    return primes
primes=seive(175143)
old1=0
old2=0
old3=0
for i in range(2,1000000):
    m=i
    distict=0
    for k in primes:
        if i%k==0:
            i=i/k
            distict+=1
    if distict==4:
        if old1+1==m and old2+1==old1 and old3+1==old2:
            print(old3,old2,old1,m)
        old3=old2
        old2=old1
        old1=m
