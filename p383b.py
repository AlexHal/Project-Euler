# Using a property of T5(n)  found by inspection.
def t55(n):
    if n == 7:
        return 26948412
    elif n==5:
        return 2264764
    elif n==6:
        return 7812294
    result = 2*t55(n-1)+5*t55(n-2)
    return result

print(t55(18))
