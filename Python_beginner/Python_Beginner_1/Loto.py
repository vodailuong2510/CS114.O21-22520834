
def my_input():
    data = input().split(" ")
    data = [int(x) for x in data]
    return data

loto = []
for i in range(3):
    loto.append(my_input())

num_num = int(input())
selected_num = []
for i in range(num_num):
    number = int(input())
    selected_num.append(number)

def win_row(loto, selected_num):
    for i in range(3):
        win = 0
        for j in range(3):
            if loto[i][j] in selected_num:
                win +=1
        if win == 3:
            return 1
    return 0
def win_col(loto, selected_num):
    for i in range(3):
        win = 0
        for j in range(3):
            if loto[j][i] in selected_num:
                win +=1
        if win == 3:
            return 1
    return 0

def win_cross(loto, selected_num):
    win = 0
    for i in range(3):
        if loto[i][i] in selected_num:
                win +=1
    if win == 3:
        return 1
    
    win = 0
    for i in range(3):
        if loto[i][3-i-1] in selected_num:
            win +=1
    if win == 3:
        return 1
    return 0

if win_row(loto, selected_num) == 1 or win_col(loto, selected_num) == 1 or win_cross(loto, selected_num) == 1:
    print('Yes')
else:
    print('No')
