import time
start_time=time.time()
f1 = 1
f2 = 1
#count_max = int(input("How many iterations> "))
#count = 2
element=[]
nth = 0
while nth<=4000000 :
    nth = f1 + f2
    #print(nth)
    if nth<=4000000 and (nth/2).is_integer():
        element.append(nth)

    f1 = f2
    f2 = nth
    #count += 1
a=0
for i in element:
    a=a+i
print(a)
endtime=time.time()
print(f"This took {start_time-endtime} seconds")
