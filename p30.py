works = []
for i in range(10,6*9**5):
    if i>=100000:
        digit1=i//100000
        digit2=i//10000-digit1*10
        digit3=i//1000-digit2*10-digit1*100
        digit4=i//100-digit3*10-digit2*100-digit1*1000
        digit5=i//10-digit4*10-digit3*100-digit2*1000-digit1*10000
        digit6=i-digit5*10-digit4*100-digit3*1000-digit2*10000-digit1*100000
        if i==digit1**5+digit2**5+digit3**5+digit4**5+digit5**5+digit6**5:
            works.append(i)
    elif i>=10000:
        digit1=i//10000
        digit2=i//1000-digit1*10
        digit3=i//100-digit2*10-digit1*100
        digit4=i//10-digit3*10-digit2*100-digit1*1000
        digit5=i-digit4*10-digit3*100-digit2*1000-digit1*10000
        if i==digit1**5+digit2**5+digit3**5+digit4**5+digit5**5:
            works.append(i)
    elif i>=1000:
        digit1=i//1000
        digit2=i//100-digit1*10
        digit3=i//10-digit2*10-digit1*100
        digit4=i-digit3*10-digit2*100-digit1*1000
        if i==digit1**5+digit2**5+digit3**5+digit4**5:
            works.append(i)
    elif i>=100:
        digit1=i//100
        digit2=i//10-digit1*10
        digit3=i-digit1*100-digit2*10
        if i==digit1**5+digit2**5+digit3**5:
            works.append(i)
    elif i>=10:
        digit1=i//10
        digit2=i-digit1*10
        if i==digit1**5+digit2**5:
            works.append(i)
print(works)
sum =0
for i in works:
    sum+=i

print(sum)
