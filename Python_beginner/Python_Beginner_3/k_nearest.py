import sys
def find_closest_numbers(arr, k, x):
    left = 0
    right = len(arr) - 1
    
    while right - left >= k:
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        else:
            right -= 1

    print(*arr[left: right + 1])

n = sys.stdin.readline()
arr = tuple(map(int, sys.stdin.readline().split()))
k, x = map(int, sys.stdin.readline().split())
find_closest_numbers(arr, k, x)