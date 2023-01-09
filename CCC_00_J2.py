def rotatable(x):
    a = str(x)
    for j in range(len(a)):
        if a[j] in ["0", "1", "8"] and a[j] != a[len(a)-j-1]:
            return False
        elif a[j] == "6" and a[len(a)-j-1] != "9":
            return False
        elif a[j] == "9" and a[len(a)-j-1] != "6":
            return False
        elif a[j] not in ["0", "1", "8", "6", "9"]:
            return False

    return True


m = int(input())
n = int(input())
count = 0
for i in range(m, n+1):
    if rotatable(i):
        count += 1

print(count)
