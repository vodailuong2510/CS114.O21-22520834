import sys
import heapq

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

online_users = []
set_online_users = set()

while True:
    data = sys.stdin.readline().split()
    if len(data) == 1:
        break
    status, user_id = int(data[0]), int(data[1])
    if status == 1 and user_id not in set_online_users:
        heapq.heappush(online_users, user_id)
        set_online_users.add(user_id)
    else:
        print(binary_search(online_users, user_id))
