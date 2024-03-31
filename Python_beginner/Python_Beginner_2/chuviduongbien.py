m,n = map(int, input().split())

matrix = []
for i in range(m):
    data = input().split()
    data = [int(x) for x in data]
    matrix.append(data)

perimeter = 0
for i in range(m):
    for j in range(n):
        around = 0
        if matrix[i][j] == 1:
            if j - 1 >= 0:
                around += matrix[i][j-1]
            if j + 1 < n:
                around += matrix[i][j+1]
            if i - 1 >= 0:
                around += matrix[i-1][j]
            if i + 1 < m:
                around += matrix[i+1][j]

            perimeter += 4 - around
print(perimeter)