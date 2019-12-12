import time
start_time=time.time()

facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def nth_digit(number, position):
    return int(number// 10**position %10)
def sum_fact_digit(number):
    sum=0
    for i in range(len(str(number))):
        sum+=facts[nth_digit(number, i)]
    return sum
sum=0
for i in range(4, 10**6):
    if i == sum_fact_digit(i):
        sum+=i
        print(i, sum)
print(sum)

endtime=time.time()
print(f"This took {abs(start_time-endtime)} seconds")
