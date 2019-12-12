import math
import time
import itertools

print("----------Start----------")
start_time=time.time()
sets = 1
seed = [1,2,5,10,20,50,100]
coefficent=[int(x) for x in range(0,101)] # =[0,1,2,3,...,98,99,100]
for L in range(1, len(seed)+1):
    for subset in itertools.combinations(seed, L):
        coefficent=[int(x) for x in range(0,101)]
        for subset_of_coeficctien in itertools.combinations(coefficent, L)
