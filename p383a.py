#Brute forceishh alot of optimization
def f5(n,x):
    if n%5==0:
        x=f5(n/5,x+1)
    return x

def t5s(n):
    start_time=time.time()
    max=3
    past=-2
    for k in range(6,int(n/5+1)):
        if k%5==4:
            continue
        if k%5==0:
            past+=-2*(f5(k/5,0)+1)
        elif k%5==1:
            past+=f5((k-1)/5,0)+1
        elif k%5==3:
            past+=f5(2*(k-3)/5+1,0)+1
        if past<0:
            max+=1
    endtime=time.time()
    print(f"Max up to now is: {max}", f"This took {abs(start_time-endtime)} seconds")
    return max


-----------------------------------------------

Other pieces of code used for previous versions of the brute force:


def f5factorial(n):
    result=0
    for i in range(1,19):
        result+= n//5**i
        if n//5**i==0:
            break
    return result


def f5(n,x):
    if n%5==0:
        x=f5(n/5,x+1)
    return x

def t5n(n):
    start_time=time.time()
    max=3
    past=-2
    for i in range(30,n+1, 5):
        k=i/5
        if k%5==0:
            past+=-2*f5(k,0)
        elif k%5==1:
            past+=f5(k-1,0)
        else:
            past+=f5(2*k-1,0)
        if past<0:
            max+=1
    endtime=time.time()
    print(f"Max up to now is: {max}", f"This took {abs(start_time-endtime)} seconds")
    print("")
    return max
    return max

def t5o(n):
    start_time=time.time()
    max=3
    past=-2
    to_check=[0,1,3,5,6,8]
    k=6
    while k< int(n/5+1):
        #print(k, past)
        if k%5==0:
            past+=-2*(f5(k/5,0)+1)
            k+=1
            if past<0:
                max+=1
        elif k%5==1:
            past+=f5((k-1)/5,0)+1
            k+=2
            if past<0:
                max+=2
        elif k%5==3:
            past+=f5(2*(k-3)/5+1,0)+1
            k+=2
            if past<0:
                max+=1
    endtime=time.time()
    print(f"Max up to now is: {max}", f"This took {abs(start_time-endtime)} seconds")
    return ma
