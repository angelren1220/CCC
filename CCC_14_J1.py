a, b, c = int(input()), int(input()),int(input())
if (a + b + c) != 180:
    print("Error")
else:
    if a==b and b==c and a==c:
        print("Equilateral")
    elif a!=b and b!=c and c!=a:
        print("Scalene")
    else:
        print("Isosceles")
