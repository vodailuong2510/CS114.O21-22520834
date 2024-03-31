import sys
m,n = map(int, sys.stdin.readline().split())

image = []
for _ in range(m):
    image.append(sys.stdin.readline())

def count_stars(image, m, n):
    visited = [[False] * n for _ in range(m)]
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n
    def dfs(x, y):
        if not is_valid(x, y) or visited[x][y] or image[x][y] == '#':
            return 0
        visited[x][y] = True
        count = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            count += dfs(x + dx, y + dy)
        return count
    star_count = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and image[i][j] == '-':
                star_count += 1
                dfs(i, j)
    return star_count

print(count_stars(image, m, n))