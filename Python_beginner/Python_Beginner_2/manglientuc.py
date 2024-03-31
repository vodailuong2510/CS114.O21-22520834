import sys
n = int(sys.stdin.readline())

matrix = []
matrix.append(int(sys.stdin.readline()))
max = matrix[0]
min = matrix[0]
for _ in range(n-1):
    num = int(sys.stdin.readline())
    matrix.append(num)
    if num > max:
        max = num
    elif num < min:
        min = num
print(max - min - len(matrix) + 1)

