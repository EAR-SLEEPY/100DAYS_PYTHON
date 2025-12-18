low=high=1
fib=0
print(low)
print(high)
for i in range(3,20):
    fib=low+high
    print(fib)
    low=high
    high=fib