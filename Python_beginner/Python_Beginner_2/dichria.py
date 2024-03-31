import sys
r,c = map(int, sys.stdin.readline().split())

matrix = []
for i in range(r):
    matrix.append(sys.stdin.readline().split())

up, down, left, right = 0, r - 1, 0 , c - 1
edge = 0
while up  <= down and left <= right:
    if left == right and edge % 2 == 0:
        temp_1 = matrix[down][left]
        for i in range(down, up, -1):
            matrix[i][left] = matrix[i-1][left]
        matrix[up][left] = temp_1
        break
    elif left == right and edge % 2 != 0:
        temp_1 = matrix[up][left]
        for i in range(up, down):
            matrix[i][left] = matrix[i+1][left]
        matrix[down][left] = temp_1
    elif down == up and edge % 2 == 0:
        temp_1 = matrix[up][right]
        for i in range(right, left, -1):
            matrix[up][i] = matrix[up][i-1]
        matrix[up][left] = temp_1
    elif down == up and edge % 2 != 0:
        temp_1 = matrix[up][left]
        for i in range(left, right):
            matrix[up][i] = matrix[up][i+1]
        matrix[up][right] = temp_1
    elif edge % 2 == 0:
        temp_1 = matrix[up][right]
        for i in range(right, left, -1):
            matrix[up][i] = matrix[up][i-1]

        temp_2 = matrix[down][right]
        for i in range(down, up, - 1):
            matrix[i][right] =  matrix[i-1][right]
            if i == up + 1:
                matrix[i][right] = temp_1

        temp_1 = matrix[down][left]
        for i in range(left, right):
            matrix[down][i] = matrix[down][i+1]
            if i == right - 1:
                matrix[down][i] = temp_2

        for i in range(up, down):
            matrix[i][left] = matrix[i+1][left]
            if i == down - 1:
                matrix[i][left] = temp_1
    else:
        temp_1 = matrix[up][left]
        for i in range(left, right):
            matrix[up][i] = matrix[up][i+1]
        
        temp_2 = matrix[down][left]
        for i in range(down, up, -1):
            matrix[i][left] = matrix[i - 1][left]
            if i == up + 1:
                matrix[i][left] = temp_1

        temp_1 = matrix[down][right]
        for i in range(right, left, -1):
            matrix[down][i] = matrix[down][i - 1]
            if i == left + 1:
                matrix[down][i] = temp_2

        for i in range(up, down):
            matrix[i][right] = matrix[i+1][right]
            if i == down - 1:
                matrix[i][right] = temp_1

    up, down, left, right = up + 1, down - 1, left + 1, right - 1
    edge += 1
for i in range(r):
    for j in range(c):
        if j != c-1:
            print(matrix[i][j], end = " ")
        else:
            print(matrix[i][j])