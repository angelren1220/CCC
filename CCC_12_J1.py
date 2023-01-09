limit = int(input())
speed = int(input())

d = speed - limit
f = 0
if d <= 0:
    print("Congratulations, you are within the speed limit!")
else:
    if 0 < d < 21:
        f = 100
    elif 20 < d < 31:
        f = 270
    else:
        f = 500
    print("You are speeding and your fine is $%d." % f)
