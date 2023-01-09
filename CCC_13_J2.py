word = input()
flag = True
for ch in word:
    if ch not in ["I", "O", "S", "H", "Z", "X", "N"]:
        print("NO")
        flag = False
        break
if flag:
    print("YES")
