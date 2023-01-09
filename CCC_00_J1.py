fd, d = input().split()
fd, d = [int(fd), int(d)]

D = ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]

for i in range(0, 7):
    if (i+1)%7 == 0:
        print(D[i], end="\n")
    else:
        print(D[i], end=" ")
for i in range(1, fd + d):
    if i - fd < 0:
        print("   ", end=" ")
    if i - fd > 0:
        if (i-1) % 7 == 0:
            print("%3d" % (i - fd), end="\n")
        else:
            print("%3d" % (i - fd), end=" ")
print("%3d" % d, end="\n")
