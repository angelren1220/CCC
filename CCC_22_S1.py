N = int(input())
solution = 0
while N >= 0:
    if N % 5 == 0:
        solution += 1
    N -= 4
print(solution)