import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(n)]

operations = tuple(sys.stdin.readline().split() for _ in range(m))

heapq.heapify(arr)

for op in operations:
    if int(op[0]) == -1:
        heapq.heappop(arr)
    elif int(op[0]) == -2:
        max_val = heapq.nlargest(1, arr)[0]
        while max_val in arr:
            arr.remove(max_val)
        heapq.heapify(arr)
    elif int(op[0]) == -3:
        decrease_amount = int(op[1])
        max_val = heapq.nlargest(1, arr)[0]
        arr[arr.index(max_val)] -= decrease_amount
        heapq.heapify(arr)
    elif int(op[0]) == -4:
        decrease_amount = int(op[1])
        max_val = heapq.nlargest(1, arr)[0]
        for i in range(len(arr)):
            if arr[i] == max_val:
                arr[i] -= decrease_amount
        heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))
