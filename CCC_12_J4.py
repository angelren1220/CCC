k = int(input())
word = input()
decode = ""
for i in range(len(word)):
    shift = 3 * (i + 1) + k
    pos = ord(word[i]) - ord('A') - shift
    while pos < 0:
        pos += 26
    decode += chr(ord('A') + pos)
print(decode)
