def remove_2s(n):
    #print("2",n)
    if n%2==0:
        n/=2
        remove_2s(n)
    else:
        return n
def remove_5s(n):
    #print("5", n)
    if n%5==0:
        n/=5
        remove_5s(n)
    else:
        return n
def purify(n):
    n=remove_2s(n)

    if n!=None:
        n=remove_5s(n)

    return n

max=9
for i in range(7,1001):
    #print(i)
    for k in range(1,1001):
        z=purify(i)
        if z==None:
            break
        elif  10**k % z==1:
            #print(i, k, 1/i)
            if k>max:
                print(i, k)
                max=k
            break
