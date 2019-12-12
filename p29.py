final = []
for i in range(2,101):
    for k in range(2,101):
        attemp =i**k
        if attemp not in final:
            final.append(attemp)
print(final)
print(len(final))
