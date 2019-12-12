import time
max_p = 150
goodprimes = [prime for prime in range(2, max_p) if prime%4==1 and all(prime%i for i in range(2,prime))]
sum_final=0
for i, prime in enumerate(goodprimes):
    for a in range(0, prime-1):
        for b in range(a, prime):
            if a*a +b*b==prime:
                goodprimes[i]=[(a,b)]
#get a number that works
print("-------Part 1------")
start_time = time.time()
print(goodprimes)
def recursion(square, index):
    global sum_final
    sum_final+=sum(min(c,d) for c,d in square)
    for i in range(index+1, len(goodprimes)):
        a,b =goodprimes[i][0]
        recursion([(abs(a*c-b*d), a*d+b*c) for c, d in square], i)
        recursion([(abs(a*d-b*c), a*c+b*d) for c, d in square], i)

for i in range(len(goodprimes)):
    recursion(goodprimes[i],i)
    print(max_p,i,sum_final,"--- %s seconds ---" % (time.time() - start_time))
