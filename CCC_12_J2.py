reading = []
for i in range(4):
    reading.append(int(input()))
if reading[0]>reading[1]>reading[2]>reading[3]:
    print("Fish Diving")
elif reading[0]<reading[1]<reading[2]<reading[3]:
    print("Fish Rising")
elif reading[0]==reading[1]==reading[2]==reading[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")
