n = int(input())
A, D = 100, 100
for i in range(n):
    r1, r2 = input().split()
    if int(r1) > int(r2):
        D -= int(r1)
    elif int(r1) < int(r2):
        A -= int(r2)
print(A)
print(D)
