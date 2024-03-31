m, n = map(int, input().split())
online_users = list(map(int, input().split()))
binh_friends = list(map(int, input().split()))
binh_friends.sort()

online_binh_friends = 0
current_index = 0

for i in range(len(binh_friends)):    
    if binh_friends[i] > online_users[-1]:
        break
    for j in range(current_index, len(online_users)):
        if online_users[j] == binh_friends[i]:
            online_binh_friends += 1
            current_index = j + 1
        elif binh_friends[i] < online_users[j]:
            break

print(online_binh_friends)