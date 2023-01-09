while True:
    s = input()
    if s == "quit!":
        break
    elif s != "quit!":
        if len(s) > 4 and s.endswith("or"):
            if s[-3] in ["a","e","i","o","u","y"]:
                print(s)
            else:
                s += " "
                print(s.replace("or ", "our"))
        else:
            print(s)


