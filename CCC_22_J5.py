N = int(input())
T = int(input())
Trees = [[0 for x in range(N)] for y in range(N)]
for i in range(T):
    x, y = input().split()
    Trees[int(x)-1][int(y)-1] = 1

print(Trees)
