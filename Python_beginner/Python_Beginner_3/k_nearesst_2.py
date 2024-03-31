import sys
def find_closest_numbers(arr, k, x, n):
    left, right = 0, n - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    print(arr[left], arr[left + k - 1])

n = int(sys.stdin.readline())
arr = tuple(map(int, sys.stdin.readline().split()))
while 1:
    data = sys.stdin.readline().strip()
    if not data:
        break
    k, x = map(int, data.split())
    find_closest_numbers(arr, k, x, n)