def my_input():
    data = []
    chars = input()
    for char in chars:
        data.append(char)
    return data

XYZ = []
for i in range(2):
    XYZ.append(my_input())

num_station = 0
for i in XYZ:
    for j in i:
        if j == '#':
            num_station +=1

if num_station == 2:
    if (XYZ[0][0] == '#' and XYZ[1][1] == '#') or (XYZ[0][1] == '#' and XYZ[1][0] == '#'):
        print("No")
    else:
        print("Yes")
else:
    print("Yes")