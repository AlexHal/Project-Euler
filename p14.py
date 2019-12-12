import time
start_time=time.time()

def turns_of(n_out, number):
    if number%2==0 and number!=1:
        n_out=1+turns_of(n_out, number/2)
    elif (number-1)%2==0 and number!=1:
        n_out=2+turns_of(n_out, (3*number+1)/2)
    return n_out
max=0
for n in range(500000, 10**6):
    if turns_of(0,n)>=max:
        print(n, turns_of(0, n))
        max=turns_of(0,n)
endtime=time.time()
print(f"This took {abs(start_time-endtime)} seconds")
