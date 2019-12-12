import time

def f5a(n):
    if n<=0:
        return 0
    result=n//5+f5a(n//5)
    return result
max=1
for i in range(10**6):
    if f5a(2*i-1)<2*f5a(i):
        max+=1
print(max)
