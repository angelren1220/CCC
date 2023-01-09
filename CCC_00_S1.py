q, f, s, t = int(input()), int(input()), int(input()), int(input())

n = 0
while q > 0:
    q -= 1
    n += 1
    f += 1
    if f == 35:
        f = 0
        q += 30
    if q == 0:
        break

    q -= 1
    n += 1
    s += 1
    if s == 100:
        s = 0
        q += 60
    if q == 0:
        break

    q -= 1
    n += 1
    t += 1
    if t == 10:
        t = 0
        q += 9
    if q == 0:
        break

print("Martha plays %d times before going broke." % n)
