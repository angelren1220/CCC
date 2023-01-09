keyword = input()
message = input()

shift = list(keyword)

for ch in message:
    if not ch.isalpha():
        message = message.replace(ch, '')
code = list(message)

for i in range(len(code)):
    for j in range(len(shift)):
        if i % len(shift) == j:
            code[i] = chr((ord(code[i]) - ord('A') + ord(shift[j]) - ord('A')) % 26 + ord('A'))


for c in code:
    print(c, end="")
