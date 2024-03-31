r, c = map(int, input().split())

matrix = []
for row in range(r):
    matrix.append(input())

row = r - 1
while (row >= 0):
    print(matrix[row])
    row -= 1
