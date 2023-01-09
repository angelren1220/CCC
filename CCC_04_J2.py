X, Y = int(input()), int(input())
m, t, c, d = 1, 1, 1, 1
for i in range(X, Y+1):
    if m == 1 and t == 1 and c == 1 and d == 1:
        print("All positions change in year %d" % i)
    m = (m+1)%4
    t = (t+1)%2
    c = (c+1)%3
    d = (d+1)%5
