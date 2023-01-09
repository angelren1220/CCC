t, s, h= int(input()), int(input()), int(input())
w = 3 + s * 2
for i in range(t):
    print("*"+" "*s+"*"+" "*s+"*")
print("*"*w)
for i in range(h):
    print(" " * (w // 2) + "*")
    
