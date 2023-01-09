N = int(input())
count = 0

for i in range(N):
    points = int(input())
    fouls = int(input())
    star = points*5-fouls*3
    if star > 40:
        count +=1
if count < N: print(count)
else: print(count, "+", sep='')