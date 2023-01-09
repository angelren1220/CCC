X = int(input())
same = dict()
for i in range(X):
    stu1, stu2 = map(hash, input().split())
    same[stu1+stu2] = 1

Y = int(input())
not_same = dict()
for i in range(Y):
    stu1, stu2 = map(hash, input().split())
    not_same[stu1+stu2] = 0

G = int(input())
for i in range(G):
    stul = list(map(hash, input().split()))
    stu = [stul[0] + stul[1], stul[1] + stul[2], stul[0] + stul[2]]
    for i in range(3):
        if stu[i] in same:
            same[stu[i]] = 0
        if stu[i] in not_same:
            not_same[stu[i]] = 1

print((sum(same.values()) + sum(not_same.values())))



