def repeated(s: str) -> bool:
    for d in s:
        if s.count(d) > 1:
            return True
    return False


year = int(input())
year += 1
while repeated(str(year)):
    year += 1
print(year)

