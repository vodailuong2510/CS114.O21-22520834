n = int(input())

matrix = []
for _ in range(n):
    matrix.append(int(input()))

def check(n, matrix):
    num = 0
    if n % 2 != 0:
        for i in range(n//2):
            if matrix[i] != matrix[n-1-i]:
                num += 1
                if num > 1:
                    return 'FALSE'
    else:
        for i in range(int(n/2)):
            if matrix[i] != matrix[n-1-i]:
                num += 1
                if num > 1:
                    return 'FALSE'
    return 'TRUE'

print(check(n, matrix))