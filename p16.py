num = 2**1000
digits = [int(x) for x in str(num)]
sum=0
print(num)
print(digits)
for i in range(0, len(str(num))):
    sum+=digits[i]
print(sum)
