import math
from time import time
t = time()
triange_num = 0
for i in range(1,1000000000):
    div=0
    triange_num += i
    for z in range(1,math.ceil(math.sqrt(triange_num))):
        if triange_num%z==0:
            div += 2
            if z*z==triange_num:
                div-=1
    if div>499:
        tt = time()-t
        print(f"{triange_num}", tt)
