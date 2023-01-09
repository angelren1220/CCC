n = int(input())
stream = []
for i in range(n):
    stream.append(int(input()))

while True:
    order = int(input())
    if order == 99:
        n, p = int(input()), int(input())
        stream.insert(n, stream[n-1]*(1-p/100))
        stream[n-1] = stream[n-1]*p/100

    elif order == 88:
        n = int(input())
        stream[n] = stream[n-1] + stream[n]
        stream.pop(n-1)

    else:
        break

for s in stream:
    print(int(s), end=" ")
