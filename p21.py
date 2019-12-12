sol = []
for i in range(0,10001):
    proper_i=0
    proper_test=0
    for k in range(1,i):
        if i%k==0:
            proper_i+=k
    for k in range(1,proper_i):
        if proper_i%k==0:
            proper_test+=k
    if proper_test==i and i!=proper_i:
        sol.append(i)


    print(i, proper_i, proper_test)
print(sol)
start =0
for amical in sol:
    start+=amical

print(start)
