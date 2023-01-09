import math
while True:
    c = int(input())
    if c == 0:
        break
    else:
        w = math.floor(math.sqrt(c))
        while c % w != 0:
            w -= 1
        l = c / w
        print("Minimum perimeter is %d with dimensions %d x %d" %(2*(w+l), w, l))

