import time
start_time = time.time()
f_1=1
f_2=1
f_n=0
digitset = set([1,2,3,4,5,6,7,8,9])
k=2
pi=1
while k<=1000:
    k+=1
    f_n = f_1+f_2
    f_1=f_2
    f_2=f_n
    startd=set([int(d) for d in str(f_n)[:9]])
    endd=set([int(d) for d in str(f_n)[-9:]])
    #if startd==endd==digitset:
    #    print(k, startd, endd, "--- %s seconds ---" % (time.time() - start_time))
    #if k>=10**pi:
    #    print(k,pi)
    #    pi+=1

start_time = time.time()
ef_1=1
ef_2=1
sf_1=1
sf_2=1
f_n=0
digitset = set([1,2,3,4,5,6,7,8,9])
k=2
pi=1
while True:
    k+=1
    ef_n = ef_1+ef_2
    ef_1=int(str(ef_2)[-10:])
    ef_2=int(str(ef_n)[-10:])

    sf_n = sf_1+sf_2
    count1=0
    number = sf_n
    while (number > 0):
        number = number//10
        count1 = count1 + 1
    number2 = sf_2
    count2=0
    while (number2 > 0):
            number2 = number2//10
            count2 = count2 + 1
    if count1>60 or count2>60:
        if count1==count2:
            sf_1=int(str(sf_2)[:60])
            sf_2=int(str(sf_n)[:60])
        else:
            sf_1=int(str(sf_2)[:60])
            sf_2=int(str(sf_n)[:60])*10
    else:
        sf_1=int(str(sf_2)[:60])
        sf_2=int(str(sf_n)[:60])
    endd=set([int(d) for d in str(ef_n)[-9:]])
    startd=set([int(d) for d in str(sf_n)[:9]])
    if endd==startd==digitset:
        print(k,startd, endd, "--- %s seconds ---" % (time.time() - start_time))
    if k>=10**pi:
        print(k, count2)
        pi+=0.2
