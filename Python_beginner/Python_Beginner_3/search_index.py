import sys

n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split())
m = sys.stdin.readline()
xs = list(sys.stdin.readline().split())

indexes = dict()
for i in range(n):
    indexes[arr[i]] = i

for x in xs:
    print(indexes.get(x, -1))