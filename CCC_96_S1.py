def sumfactors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum


n = int(input())
for i in range(n):
    x = int(input())
    if x > sumfactors(x):
        print("%d is a deficient number." % x)
    elif x == sumfactors(x):
        print("%d is a perfect number." % x)
    else:
        print("%d is an abundant number." % x)
