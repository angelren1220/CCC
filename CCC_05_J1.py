daytime = int(input())
evening = int(input())
weekend = int(input())
Acost = evening * 15 + weekend * 20
Bcost = evening * 35 + weekend * 25
if daytime > 100:
    Acost += (daytime - 100) * 25
if daytime > 250:
    Bcost += (daytime - 250) * 45
Acost /= 100.00
Bcost /= 100.00


print("Plan A costs %.2f" % Acost)
print("Plan B costs %.2f" % Bcost)
if Acost > Bcost:
    print("Plan B is cheapest.")
elif Acost < Bcost:
    print("Plan A is cheapest.")
else:
    print("Plan A and B are the same price.")



