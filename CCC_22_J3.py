string = input()
instruction = ""
flag = False
for ch in string:
    if ch.isalpha():
        if flag:
            instruction +="\n"
            flag = False
        instruction += ch
    elif ch == "+":
        instruction += " tighten "
    elif ch == "-":
        instruction += " loosen "
    elif ch.isdigit():
        flag = True
        instruction += ch

print(instruction)

