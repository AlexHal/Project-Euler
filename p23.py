import math
import time
start_time = time.time()


sumtocompute = [0]*28124



def getDivisors(num):
    if num==1:
        return 1
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while (divisor < n):
        if (num%divisor == 0):
            total += divisor
            total += num//divisor
        divisor+=1
    if n**2==num:
        total+=n
    return total

def isAbundant(num):
    if (getDivisors(num) > num):
        return True
    else:
        return False

abundentNums = []
for x in range (0,28124):
    if (isAbundant(x)):
        abundentNums.append(x)
del abundentNums[0]

for i in range(0,len(abundentNums)):
    for k in range(i,len(abundentNums)):
        term=abundentNums[i]+abundentNums[k]
        if term<=28123 and sumtocompute[term]==0:
            sumtocompute[term]=term
sum=0
for i in range(1, len(sumtocompute)):
    if sumtocompute[i]==0:

        sum+=i
print(sum)
print("--- %s seconds ---" % (time.time() - start_time))
