f1 = 1
f2 = 1
#count_max = int(input("How many iterations> "))
count = 2
blip=1
while blip==1:
    nth = f1 + f2
    f1 = f2
    f2 = nth
    count += 1
    if len(str(nth))==1000:
        print(f"{nth}, with index {count}")
        blip=2
