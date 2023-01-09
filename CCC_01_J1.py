h = int(input())

for i in range(h//2):
    print("*"*(2*i+1)+(2*h-2*(2*i+1))*" "+"*"*(2*i+1))

for i in reversed(range(h//2+1)):
    print("*"*(2*i+1)+(2*h-2*(2*i+1))*" "+"*"*(2*i+1))
