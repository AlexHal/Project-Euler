import math

def pentagonal(n):
    return n*(3*n-1)/2

def arcpenta(n):
    return ((1/6)*(1+math.sqrt(24*n+1))).is_integer()
def arcpentago(n):
    return ((1+math.sqrt(24*n+1)))/6
max=1000000
sets=[]
for i in range(3,max):
    for k in range(i+1,max):
        if arcpenta(pentagonal(i)+pentagonal(k)):
            #print(i,k,arcpentago(pentagonal(i)+pentagonal(k)))
            if arcpenta(pentagonal(k)-pentagonal(i)):
                print("youppiiii",i,k,arcpentago(pentagonal(k)-pentagonal(i)), pentagonal(k)-pentagonal(i))
                sets.append(pentagonal(k)-pentagonal(i))
            else:
                break
print(sets)
