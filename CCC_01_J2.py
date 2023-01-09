x = int(input())
m = int(input())
n = 1
while n < m:
    if (x * n) % m == 1:
        print(n)
        break
    else:
        n += 1
if n >= m:
    print("No such integer exists.")

