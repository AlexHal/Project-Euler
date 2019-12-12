list=[]
max=0
test_set=set(k for k in range(1,10))
print(test_set)
for i in range(1,99999):
    string=""

    for k in range(1,10):
        string+=str(int(k*i))
        if len(string)>8:
            break
    if len(string)==9 and set(int(k) for k in string)==test_set:
        if int(string)>= int(max) :
            max=string
            print(max,i,k)

print(max)
