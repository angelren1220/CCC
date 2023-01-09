lower = int(input())
upper = int(input())
count = 0
for i in range(lower, upper + 1):
    n_divisors = 0
    for j in range(1, i+1):
        if i%j == 0:
            n_divisors +=1
    if n_divisors == 4:
        count += 1
print("The number of RSA numbers between %d and %d is %d" % (lower, upper, count))
